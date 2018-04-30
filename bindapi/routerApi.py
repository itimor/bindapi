# -*- coding: utf-8 -*-
# author: kiven

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from bind.views import DomainViewSet, RecordViewSet, AllDomainViewSet, XfrAclViewSet

router.register(r'domains', DomainViewSet)
router.register(r'records', RecordViewSet)
router.register(r'xfracls', XfrAclViewSet)
router.register(r'alldomains', AllDomainViewSet, base_name='alldomains')

from analyze.views import DomainNodeViewSet, DomainStatusViewSet

router.register(r'domainnodes', DomainNodeViewSet)
router.register(r'domainstatus', DomainStatusViewSet)
