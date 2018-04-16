# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from bind.models import Domain, Record, Acl
from bind.serializers import DomainSerializer, RecordSerializer, AclSetSerializer


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
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
