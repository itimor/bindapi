# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from zkmanager.models import ZkUser, Punch, PunchSet
from zkmanager.serializers import ZkUserSerializer, PunchSerializer, PunchSetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from zkmanager.zkapi import getAllUserInfo, getReadAllGLogData
from zkmanager.filters import PunchFilter


class ZkUserViewSet(viewsets.ModelViewSet):
    queryset = ZkUser.objects.all()
    serializer_class = ZkUserSerializer
    filter_fields = ['user_id', 'username']


class PunchViewSet(viewsets.ModelViewSet):
    queryset = Punch.objects.all()
    serializer_class = PunchSerializer
    filter_class = PunchFilter


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
    queryset = getReadAllGLogData()
    punchset = PunchSet.objects.all()[0]
    for item in queryset:
        if punchset.swork_stime < item['create_time'] < punchset.swork_etime:
            if item['create_time'] > punchset.swork_time:
                item['status'] = 3
            else:
                item['status'] = 1
        elif punchset.ework_stime < item['create_time'] < punchset.ework_etime:
            if item['create_time'] < punchset.ework_time:
                item['status'] = 4
            else:
                item['status'] = 2
        else:
            item['status'] = 0
        Punch.objects.update_or_create(**item)
    return Response(queryset)
