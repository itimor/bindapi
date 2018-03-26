# -*- coding: utf-8 -*-
# author: kiven

from django.conf.urls import url, include
from zkapi.routerApi import router
from zkmanager.views import getzkuser
from zkmanager.views import getpunch

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/getzkuser/', getzkuser, name="getzkuser"),
    url(r'^api/getpunch/', getpunch, name="getpunch"),
]
