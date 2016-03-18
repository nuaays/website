# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: user_details.py
time   : 16/3/18 下午4:05  
"""
from django.db import models
from website.models.user import User
from django.utils.translation import ugettext_lazy as _


class UserDetail(models.Model):
    email = models.EmailField(max_length=256, )
    password = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True)
    name = models.CharField(max_length=256, null=True)
    company = models.CharField(max_length=256, null=True)
    server_count = models.IntegerField(null=True)
    user = models.ForeignKey(User)
    org_name = models.CharField(max_length=128, null=True)
    domain_name = models.CharField(max_length=128, null=True)

    class Meta:
        app_label = 'website'
        db_table = 'user_details'
        verbose_name = _('user details')
        verbose_name_plural = _('users details')