# -*- coding: utf-8 -*-
# author: kiven

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from zkmanager.views import UserViewSet

router.register(r'users', UserViewSet)
