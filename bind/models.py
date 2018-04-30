# -*- coding: utf-8 -*-
# author: itimor

from django.db import models


class Domain(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=u"域名")
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

Record_Status = {
    'enable': 'enable',
    'disabled': 'disabled'
}


class Record(models.Model):
    title = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=u"记录全名")
    # zone = models.ForeignKey(Domain, on_delete=models.CASCADE, verbose_name=u"所在域")
    zone = models.CharField(max_length=100, verbose_name=u"域名")
    name = models.CharField(max_length=30, verbose_name=u"记录名")
    type = models.CharField(choices=Types.items(), default='A', max_length=10, verbose_name=u"记录类型")
    value = models.CharField(max_length=50, verbose_name=u"记录值")
    status = models.CharField(choices=Record_Status.items(), default='enable', max_length=11, verbose_name=u'状态')
    ttl = models.IntegerField(default=600, verbose_name=u"缓存时间")
    mx = models.IntegerField(null=True, blank=True, verbose_name=u"mx记录优先级")
    serial = models.BigIntegerField(null=True, blank=True, verbose_name=u"SOA记录的序列号")
    refresh = models.IntegerField(null=True, blank=True, verbose_name=u"SOA记录的刷新时间")
    retry = models.IntegerField(null=True, blank=True, verbose_name=u"SOA记录的重试时间")
    expire = models.IntegerField(null=True, blank=True, verbose_name=u"SOA记录的过期时间")
    minimum = models.IntegerField(null=True, blank=True, verbose_name=u"SOA记录的minimum")
    resp_person = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"域名管理者")
    primary_ns = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"主ns")
    data_count = models.IntegerField(null=True, blank=True, verbose_name=u"统计")
    tan = models.BooleanField(default=False, verbose_name=u"是否探测")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u"创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name=u"更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '记录'
        verbose_name_plural = '记录'

    def save(self, *args, **kwargs):
        self.title = '{}-{}-{}-{}'.format(self.zone, self.name, self.type, self.value)
        super(Record, self).save(*args, **kwargs)