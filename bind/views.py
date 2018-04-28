# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from bind.models import Domain, Record
from bind.serializers import DomainSerializer, RecordSerializer
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.permissions import IsAdminUser


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = (IsAdminUser,)
    filter_fields = ['name', 'create_time']
    search_fields = ['name']


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by('create_time')
    serializer_class = RecordSerializer
    permission_classes = (IsAdminUser,)
    filter_fields = ['domain__name', 'name', 'value', 'create_time']
    search_fields = ['name', 'value']


class AllDomainViewSet(viewsets.ViewSet):

    def list(self, request):
        allurls = []
        domains = Domain.objects.all()
        for domain in domains:
            suffix = domain.name
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
                if prefix != '@' and record.tan:
                    allurls.append(prefix + '.' + suffix)
        return Response(allurls)
