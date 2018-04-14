# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from django.contrib.auth.models import User


class Zone(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"域名")
    create_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=u"创建者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u"创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name=u"更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '域'
        verbose_name_plural = '域'


Types = {
    'A': 'A', 'MX': 'MX', 'CNAME': 'CNAME',
    'NS': 'NS', 'SOA': 'SOA', 'PTR': 'PTR',
    'TXT': 'TXT', 'AAAA': 'AAAA', 'SVR': 'SVR', 'URL': 'URL'
}


class Record(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, verbose_name=u"所在域")
    name = models.CharField(max_length=30, verbose_name=u"记录名")
    type = models.CharField(choices=Types.items(), default='A', max_length=10, verbose_name=u"记录类型")
    value = models.CharField(max_length=255, verbose_name=u"记录值")
    ttl = models.IntegerField(default=600, verbose_name=u"缓存时间")
    mx_priority = models.IntegerField(null=True, blank=True, verbose_name=u"mx记录优先级")
    serial = models.BigIntegerField(null=True, blank=True, verbose_name=u"SOA记录的序列号")
    refresh = models.IntegerField(null=True, blank=True, verbose_name=u"SOA记录的刷新时间")
    retry = models.IntegerField(null=True, blank=True, verbose_name=u"SOA记录的重试时间")
    expire = models.IntegerField(null=True, blank=True, verbose_name=u"SOA记录的过期时间")
    minimum = models.IntegerField(null=True, blank=True, verbose_name=u"SOA记录的minimum")
    resp_person = models.CharField(max_length=64, null=True, blank=True, verbose_name=u"SOA记录负责人")
    primary_ns = models.CharField(max_length=64, null=True, blank=True, verbose_name=u"主dns")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u"创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name=u"更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '记录'
        verbose_name_plural = '记录'


class Acl(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, verbose_name=u"所在域")
    client = models.CharField(max_length=255, verbose_name=u"记录名")

    class Meta:
        verbose_name = 'Acl'
        verbose_name_plural = 'Acl'
