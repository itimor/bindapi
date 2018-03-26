# -*- coding: utf-8 -*-
# author: kiven

from .models import ZkUser, Punch
from rest_framework import serializers


class ZkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZkUser
        fields = ('url', 'user_id', 'username', 'password', 'role', 'is_active')


class PunchSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=ZkUser.objects.all(), slug_field='username')

    class Meta:
        model = Punch
        fields = ('url', 'id', 'user', 'verifymode', 'create_time')
