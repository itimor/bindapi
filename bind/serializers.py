# -*- coding: utf-8 -*-
# author: kiven

from bind.models import Zone, Record, Acl
from django.contrib.auth.models import User
from rest_framework import serializers


class ZoneSerializer(serializers.ModelSerializer):
    create_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Zone
        fields = ('url', 'id', 'name', 'create_user', 'create_time', 'update_time')


class RecordSerializer(serializers.ModelSerializer):
    zone = serializers.SlugRelatedField(queryset=Zone.objects.all(), slug_field='name')

    class Meta:
        model = Record
        fields = (
            'url', 'id', 'zone', 'name', 'type', 'value', 'ttl', 'mx_priority', 'refresh', 'retry', 'expire', 'minimum',
            'serial', 'resp_person', 'primary_ns', 'create_time', 'update_time')


class AclSetSerializer(serializers.ModelSerializer):
    zone = serializers.SlugRelatedField(queryset=Zone.objects.all(), slug_field='name')

    class Meta:
        model = Acl
        fields = ('url', 'id', 'zone', 'client')
