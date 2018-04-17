# -*- coding: utf-8 -*-
# author: itimor

from django.db import models


class DomainNode(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=u"节点名称")
    ip = models.GenericIPAddressField(unique=True, verbose_name=u"节点ip")
    address = models.CharField(max_length=100, verbose_name=u"节点所在地")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '节点'
        verbose_name_plural = '节点'


class DomainStatus(models.Model):
    node = models.ForeignKey(DomainNode, on_delete=models.CASCADE, verbose_name=u"节点")
    url = models.CharField(max_length=100, verbose_name=u"域名")
    ip = models.CharField(max_length=100, verbose_name=u"解析ip")
    status = models.CharField(max_length=100, verbose_name=u"状态")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u"创建时间")

    class Meta:
        verbose_name = '域名状态'
        verbose_name_plural = '域名状态'

