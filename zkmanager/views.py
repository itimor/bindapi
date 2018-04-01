# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from zkmanager.models import ZkUser, Punch, PunchSet
from zkmanager.serializers import ZkUserSerializer, PunchSerializer, PunchSetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from zkmanager.zkapi import getAllUserInfo, getReadAllGLogData
from zkmanager.filters import PunchFilter
from zkmanager.utils import diff_times_in_seconds
from datetime import datetime


class ZkUserViewSet(viewsets.ModelViewSet):
    queryset = ZkUser.objects.all()
    serializer_class = ZkUserSerializer
    search_fields = ['user_id', 'username']


class PunchViewSet(viewsets.ModelViewSet):
    queryset = Punch.objects.all().order_by('user_id', 'create_date')
    serializer_class = PunchSerializer
    filter_class = PunchFilter
    search_fields = ['user__username']


class PunchSetViewSet(viewsets.ModelViewSet):
    queryset = PunchSet.objects.all()
    serializer_class = PunchSetSerializer


@api_view()
def getzkuser(request):
    queryset = getAllUserInfo()
    for item in queryset:
        ZkUser.objects.update_or_create(**item)
    return Response(queryset)


@api_view()
def getpunch(request, cur_date=None):
    punchset = PunchSet.objects.all()[0]
    if not cur_date:
        cur_date = datetime.now().strftime('%Y-%m-%d')
    queryset = getReadAllGLogData(cur_date)
    punchusers = []
    for i in queryset:
        punchusers.append(i["user_id"])
    zkusers = ZkUser.objects.all()
    zkpunchusers = []
    for i in zkusers:
        zkpunchusers.append(i.user_id)
    for user in zkpunchusers:
        punch = dict()
        if user in punchusers:
            for item in queryset:
                if item["user_id"] in zkpunchusers:
                    if punchset.swork_stime < item['create_time'] < punchset.swork_etime:
                        punch['swork_time'] = item['create_time']
                        if item['create_time'] > punchset.swork_time:
                            punch['swork_timec'] = diff_times_in_seconds(punchset.swork_time, item['create_time'])
                            punch['swork_status'] = 1
                        else:
                            punch['swork_status'] = 0

                    elif punchset.ework_stime < item['create_time'] < punchset.ework_etime:
                        punch['ework_time'] = item['create_time']
                        if item['create_time'] < punchset.ework_time:
                            punch['ework_timec'] = diff_times_in_seconds(item['create_time'], punchset.swork_time)
                            punch['ework_status'] = 1
                        else:
                            punch['ework_status'] = 0
                    Punch.objects.update_or_create(user_id=item["user_id"], create_date=cur_date, defaults=punch)
                else:
                    print('this user %s was deleted!' % item["user_id"])
        else:
            punch['user_id'] = user
            punch['create_date'] = cur_date
            punch['nowork_status'] = True
            p = Punch.objects.create(**punch)
            p.save()
    return Response(queryset)
