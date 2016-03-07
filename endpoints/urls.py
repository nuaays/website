# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from django.conf.urls import patterns, url
from endpoints.endpoint import HelloView, HostView,AccessTokenView
# Routers provide an easy way of automatically determining the URL conf

urlpatterns = patterns('',
                       url(r'^hello', HelloView.as_view(), name='hello'),
                       url(r'^hosts', HostView.as_view(), name='host'),
                       url(r'^access_token', AccessTokenView.as_view(), name='access-token'),
                       )