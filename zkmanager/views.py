# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from zkmanager.serializers import UserSerializer
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['username']
    filter_fields = ['id']
