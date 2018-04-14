# -*- coding: utf-8 -*-
# author: kiven

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from bind.views import ZoneViewSet, RecordViewSet, AclSetViewSet

router.register(r'zones', ZoneViewSet)
router.register(r'records', RecordViewSet)
router.register(r'acls', AclSetViewSet)
