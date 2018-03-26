# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from .models import ZkUser, Punch
from zkmanager.serializers import ZkUserSerializer, PunchSerializer


class ZkUserViewSet(viewsets.ModelViewSet):
    queryset = ZkUser.objects.all()
    serializer_class = ZkUserSerializer
    filter_fields = ['user_id', 'username']


class PunchViewSet(viewsets.ModelViewSet):
    queryset = Punch.objects.all()
    serializer_class = PunchSerializer
    filter_fields = ['user__username']