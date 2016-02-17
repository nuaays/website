# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from django.contrib.auth.models import User, Group
from django.contrib import admin
admin.autodiscover()

from rest_framework import permissions, viewsets
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from endpoints.serializer import UserSerializer, GroupSerializer

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer