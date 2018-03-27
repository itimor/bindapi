# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from zkmanager.models import ZkUser, Punch, PunchSet
from zkmanager.serializers import ZkUserSerializer, PunchSerializer, PunchSetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from zkmanager.zkapi import getAllUserInfo, getReadAllGLogData
from zkmanager.filters import PunchFilter
from datetime import datetime, timedelta


class ZkUserViewSet(viewsets.ModelViewSet):
    queryset = ZkUser.objects.all()
    serializer_class = ZkUserSerializer
    search_fields = ['user_id', 'username']


class PunchViewSet(viewsets.ModelViewSet):
    queryset = Punch.objects.all()
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
def getpunch(request):
    punchset = PunchSet.objects.all()[0]
    queryset = getReadAllGLogData()
    punchusers = []
    for i in queryset:
        punchusers.append(i["user_id"])
    zkusers = ZkUser.objects.all()
    punch = dict()
    for user in zkusers:
        if str(user.user_id) in punchusers:
            for item in queryset:
                punch['ework_timec'] = punch['swork_timec'] = '00:00:00'
                if punchset.swork_stime < item['create_time'] < punchset.swork_etime:
                    punch['swork_time'] = item['create_time']
                    if item['create_time'] > punchset.swork_time:
                        punch['swork_timec'] = diff_times_in_seconds(punchset.swork_time, item['create_time'])
                        punch['swork_status'] = False
                    else:
                        punch['swork_status'] = True
                elif punchset.ework_stime < item['create_time'] < punchset.ework_etime:
                    punch['ework_time'] = item['create_time']
                    if item['create_time'] < punchset.ework_time:
                        punch['ework_timec'] = diff_times_in_seconds(item['create_time'], punchset.swork_time)
                        punch['ework_status'] = False
                    else:
                        punch['ework_status'] = True
                Punch.objects.update_or_create(user_id=item['user_id'], create_date=item['create_date'], defaults=punch)
        else:
            punch['user_id'] = user.user_id
            punch['nowork_status'] = True
            p = Punch.objects.create(**punch)
            p.save()
    return Response(queryset)


def diff_times_in_seconds(t1, t2):
    h1, m1, s1 = t1.hour, t1.minute, t1.second
    h2, m2, s2 = t2.hour, t2.minute, t2.second
    t1_secs = s1 + 60 * (m1 + 60 * h1)
    t2_secs = s2 + 60 * (m2 + 60 * h2)
    tc = str(timedelta(seconds=(t2_secs - t1_secs)))
    return tc
