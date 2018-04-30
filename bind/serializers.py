# -*- coding: utf-8 -*-
# author: kiven

from bind.models import Domain, Record
from rest_framework import serializers


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ('url', 'id', 'name', 'create_time', 'update_time')


class RecordSerializer(serializers.ModelSerializer):
    # zone = serializers.SlugRelatedField(queryset=Domain.objects.all(), slug_field='name')

    class Meta:
        model = Record
        fields = (
            'url', 'id', 'title', 'zone', 'name', 'type', 'value', 'ttl', 'status', 'mx', 'serial',
            'refresh', 'retry', 'expire', 'minimum', 'resp_person', 'data_count', 'tan', 'create_time', 'update_time')
