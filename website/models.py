from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import datetime


# Create your models here.

def datetime_now():
    return datetime.datetime.now()


class Organization(models.Model):
    organization_name = models.CharField(max_length=128, unique=True)
    domain_name = models.CharField(max_length=256, unique=True)
    sentry_instance = models.CharField(max_length=256, unique=True)


class UserDetail(models.Model):
    email = models.EmailField(max_length=256, )
    password = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True)
    name = models.CharField(max_length=256, null=True)
    company = models.CharField(max_length=256, null=True)
    server_count = models.IntegerField(null=True)
    user = models.ForeignKey(User)
    organization = models.ForeignKey(Organization)

    def send_activation_email(self, site):
        pass

#
# class SentryInstance(models):
#     host_name = models.CharField(max_length=128,null=True)
#     ip = models.CharField(max_length=50, null=True)
#     url_prefix = models.CharField(max_length=256, null=True)
#     # user = models.ForeignKey(User)
#
