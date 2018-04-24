# -*- coding: utf-8 -*-
# author: kiven

from django.conf.urls import url, include
from bindapi.routerApi import router
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/api-token-auth/', obtain_auth_token, name='rest_framework_token'),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
