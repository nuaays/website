from django.conf.urls import patterns, include, url
from django.contrib import admin
import endpoints
admin.autodiscover()
import endpoints.urls as RestUrl
urlpatterns = patterns(
    '',
    url(r'^api/0/', include('endpoints.urls'), name='api'),
    url(r'', include('example.urls'), name='example'),
    url(r'', include('website.urls'), name='website'),
    url(r'^admin/', include(admin.site.urls)),
)
