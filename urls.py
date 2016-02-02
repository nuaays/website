from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
#
# from example.views import (
#     ConsumerView, ConsumerExchangeView, ConsumerDoneView, ApiEndpoint, ApiClientView
# )
# from example.api_v1 import get_system_info, applications_list, applications_detail


admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'', include('example.urls'), name='example'),
    # api stuff to test server functionalities

    url(r'^', include('website.urls'), name='website'),
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

)
