from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserDetail(models.Model):
  email = models.EmailField(max_length=256, )
  password = models.CharField(max_length=128, null=True, blank=True)
  phone = models.CharField(max_length=12, null=True)
  name = models.CharField(max_length=256, null=True)
  company = models.CharField(max_length=256, null=True)
  server_count = models.IntegerField(null=True)
  user = models.ForeignKey(User)
