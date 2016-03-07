# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from rest_framework import serializers
from django.contrib.auth.models import User, Group
from oauth2_provider.models import AccessToken


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


class AccessTokenSerializer(serializers.ModelSerializer):
    class meta:
        model= AccessToken