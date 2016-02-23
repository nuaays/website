# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm

class UserRegisterForm(UserCreationForm):
    pass
    # email = models.EmailField(max_length=256, )
    # password = models.CharField(max_length=128, null=True, blank=True)
    # phone = models.CharField(max_length=12, null=True)
    # name = models.CharField(max_length=256, null=True)
    # company = models.CharField(max_length=256, null=True)
    # server_count = models.IntegerField(null=True)
    # user = models.ForeignKey(User)
    # org_name = models.CharField(max_length=128, null=True)
    # domain_name = models.CharField(max_length=128, null=True)

