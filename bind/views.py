# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from bind.models import Zone, Record, Acl
from bind.serializers import ZoneSerializer, RecordSerializer, AclSetSerializer


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    filter_fields = ['name', 'create_time']
    search_fields = ['name']


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by('create_time')
    serializer_class = RecordSerializer
    filter_fields = ['zone__name', 'name', 'value', 'create_time']
    search_fields = ['name', 'value']


class AclSetViewSet(viewsets.ModelViewSet):
    queryset = Acl.objects.all()
    serializer_class = AclSetSerializer
