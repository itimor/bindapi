# -*- coding: utf-8 -*-
# author: kiven

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'username', 'password', 'is_active', 'is_superuser', 'is_staff')
