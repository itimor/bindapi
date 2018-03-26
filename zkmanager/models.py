# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from django.utils import timezone


class ZkUser(models.Model):
    user_id = models.IntegerField(primary_key=True, unique=True, verbose_name=u"用户号")
    username = models.CharField(max_length=30, verbose_name=u"用户名")
    password = models.CharField(max_length=30, null=True, blank=True, verbose_name=u"密码")
    role = models.CharField(max_length=30, default=0, verbose_name=u"身份")
    is_active = models.BooleanField(verbose_name=u"启用")

    def __str__(self):
        return self.username


Punch_Status = {
    0: '无效',
    1: '签到',
    2: '签退',
    3: '迟到',
    4: '早退'
}


class Punch(models.Model):
    user = models.ForeignKey('ZkUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u"用户")
    verifymode = models.CharField(max_length=30, default=1, verbose_name=u"打卡模式")
    status = models.CharField(max_length=1, choices=Punch_Status.items(), default=0, verbose_name=u'打卡状态')
    create_time = models.DateTimeField(default=timezone.now, verbose_name=u'打卡时间')
    create_date = models.DateField(default=timezone.now, verbose_name=u'打卡日期')


class PunchSet(models.Model):
    swork_time = models.TimeField(default=timezone.now, verbose_name=u'上班时间')
    ework_time = models.TimeField(default=timezone.now, verbose_name=u'下班时间')
    swork_stime = models.TimeField(default=timezone.now, verbose_name=u'上班打卡开始时间')
    swork_etime = models.TimeField(default=timezone.now, verbose_name=u'上班打卡结束时间')
    ework_stime = models.TimeField(default=timezone.now, verbose_name=u'下班打卡开始时间')
    ework_etime = models.TimeField(default=timezone.now, verbose_name=u'下班打卡结束时间')
    timeout = models.CharField(max_length=30, default=0, verbose_name=u"允许超时分钟")
