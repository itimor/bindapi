# -*- coding: utf-8 -*-
# author: kiven

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from zkmanager.views import ZkUserViewSet, PunchViewSet, PunchSetViewSet

router.register(r'zkusers', ZkUserViewSet)
router.register(r'zkpunchs', PunchViewSet)
router.register(r'zkpunchset', PunchSetViewSet)
