# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from bind.models import Domain, Record, XfrAcl
from bind.serializers import DomainSerializer, RecordSerializer, XfrAclSerializer
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class XfrAclViewSet(viewsets.ModelViewSet):
    queryset = XfrAcl.objects.all()
    serializer_class = XfrAclSerializer
    permission_classes = (IsAdminUser,)
    filter_fields = ['domain__name', 'client']


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
