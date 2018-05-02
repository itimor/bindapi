# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from bind.models import Domain, Record, XfrAcl
from bind.serializers import DomainSerializer, RecordSerializer, XfrAclSerializer
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from django.http import Http404


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
        self.perform_create(serializer)

        try:
            domain = request.data['domain']
            record = Record.objects.filter(domain__name=domain, type='SOA')[0]
            record.serial = record.serial + 1
            record.save()
        except:
            content = {'msg': '域名%s没有SOA记录' % request.data['domain']}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        try:
            domain = request.data['domain']
            record = Record.objects.filter(domain__name=domain, type='SOA')[0]
            record.serial = record.serial + 1
            record.save()
        except:
            content = {'msg': '域名%s没有SOA记录' % request.data['domain']}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            domain = instance.domain
            record = Record.objects.filter(domain__name=domain, type='SOA')[0]
            record.serial = record.serial + 1
            record.save()
            self.perform_destroy(instance)
        except:
            content = {'msg': '域名没有SOA记录'}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_204_NO_CONTENT)


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
