# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from bind.models import Domain, Record, Acl
from bind.serializers import DomainSerializer, RecordSerializer, AclSetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    filter_fields = ['name', 'create_time']
    search_fields = ['name']


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by('create_time')
    serializer_class = RecordSerializer
    filter_fields = ['domain__name', 'name', 'value', 'create_time']
    search_fields = ['name', 'value']


class AclSetViewSet(viewsets.ModelViewSet):
    queryset = Acl.objects.all()
    serializer_class = AclSetSerializer


@api_view()
def getallurls(request):
    allurls = []
    domains = Domain.objects.all()
    for domain in domains:
        suffix = domain.name
        allurls.append(suffix)
        records = Record.objects.filter(
            Q(domain__name=suffix) &
            (
                Q(type='A') |
                Q(type='CNAME') |
                Q(type='TXT') |
                Q(type='MX')
            )
        )
        for record in records:
            prefix = record.name
            if prefix != '@':
                allurls.append(prefix + '.' + suffix)

    return Response(allurls)
