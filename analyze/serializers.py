# -*- coding: utf-8 -*-
# author: kiven

from analyze.models import DomainNode, DomainStatus
from rest_framework import serializers


class DomainNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainNode
        fields = ('url', 'id', 'name', 'ip', 'address')


class DomainStatusSerializer(serializers.ModelSerializer):
    node = serializers.SlugRelatedField(queryset=DomainNode.objects.all(), slug_field='name')

    class Meta:
        model = DomainStatus
        fields = ('url', 'id', 'node', 'domain', 'status', 'create_time', 'create_date')
