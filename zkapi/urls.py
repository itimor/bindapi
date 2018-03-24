# -*- coding: utf-8 -*-
# author: kiven

from django.conf.urls import url, include
from zkapi.routerApi import router

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
