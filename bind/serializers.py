# -*- coding: utf-8 -*-
# author: kiven

from bind.models import Domain, Record, Acl
from django.contrib.auth.models import User
from rest_framework import serializers


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ('url', 'id', 'name', 'create_time', 'update_time')


class RecordSerializer(serializers.ModelSerializer):
    domain = serializers.SlugRelatedField(queryset=Domain.objects.all(), slug_field='name')

    class Meta:
        model = Record
        fields = (
            'url', 'id', 'title', 'domain', 'name', 'type', 'value', 'ttl', 'mx_priority', 'serial', 'refresh', 'retry', 'expire',
            'minimum', 'resp_person', 'primary_ns', 'create_time', 'update_time')


class AclSetSerializer(serializers.ModelSerializer):
    domain = serializers.SlugRelatedField(queryset=Domain.objects.all(), slug_field='name')

    class Meta:
        model = Acl
        fields = ('url', 'id', 'domain', 'client')
