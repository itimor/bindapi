# -*- coding: utf-8 -*-
# author: kiven

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from zkmanager.views import ZkUserViewSet, PunchViewSet

router.register(r'zkusers', ZkUserViewSet)
router.register(r'zkpunchs', PunchViewSet)
