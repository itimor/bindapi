# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from .models import ZkUser, Punch
from zkmanager.serializers import ZkUserSerializer, PunchSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .zkapi import getAllUserInfo, getReadAllGLogData


class ZkUserViewSet(viewsets.ModelViewSet):
    queryset = ZkUser.objects.all()
    serializer_class = ZkUserSerializer
    filter_fields = ['user_id', 'username']


class PunchViewSet(viewsets.ModelViewSet):
    queryset = Punch.objects.all()
    serializer_class = PunchSerializer
    filter_fields = ['user__username']


@api_view()
def getzkuser(request):
    queryset = getAllUserInfo()
    for item in queryset:
        ZkUser.objects.update_or_create(**item)
    return Response(queryset)


@api_view()
def getpunch(request):
    queryset = getReadAllGLogData()
    for item in queryset:
        Punch.objects.update_or_create(**item)
    return Response(queryset)
