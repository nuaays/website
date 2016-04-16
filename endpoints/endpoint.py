# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from django.contrib.auth.models import User, Group
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

from rest_framework.response import Response
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from endpoints.serializer import UserSerializer, GroupSerializer
from oauth2_provider.models import AccessToken
import requests
# ViewSets define the view behavior.
from django.contrib.auth import get_user_model
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    required_scopes = ['read']
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]

    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class HostView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read']
    """
    url: /api/0/hosts
    method: POST
    param: user_id
    param: host_type
    param: host_name
    param: distver
    param: system
    """
    def post(self, request):
        result = request.POST
        if result:
            host_instance = {'host_name': result.get('host_name', ''),
                             'host_type': result.get('host_type', ''),
                             'distver': result.get('distver', ''),
                             'system': result.get('system', ''),
                             'user_id': request.user.id}
            print result['host_type']
            url = settings.SENTRY_API + '/agent/hosts'
            r = requests.post(url=url, data=host_instance)
            return Response(r.text)

    def get(self, request):
        return Response(settings.SENTRY_INSTANCES)


class HelloView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read']

    def get(self, request):
        return Response("hello world")


class AccessTokenView(APIView):
    authentication_classes = []
    permission_classes = []
    required_scopes = ['read']

    def get(self, request):
        authorization = request.META['HTTP_AUTHORIZATION']
        token = authorization.split(" ")[1]
        access_token = AccessToken.objects.get(token=token)
        if access_token:
            return Response({'user_id': access_token.user_id})
        return Response({'ret': 'false'})