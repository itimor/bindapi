# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from analyze.models import DomainNode, DomainStatus
from analyze.serializers import DomainNodeSerializer, DomainStatusSerializer


class DomainNodeViewSet(viewsets.ModelViewSet):
    queryset = DomainNode.objects.all()
    serializer_class = DomainNodeSerializer
    filter_fields = ['name', 'ip']


class DomainStatusViewSet(viewsets.ModelViewSet):
    queryset = DomainStatus.objects.all()
    serializer_class = DomainStatusSerializer
    filter_fields = ['node__name', 'url']
