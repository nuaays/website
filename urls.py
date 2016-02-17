from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import endpoints.urls as RestUrl
urlpatterns = patterns(
    '',
    url(r'^api/0/', include(RestUrl.router.urls)),
    url(r'', include('example.urls'), name='example'),
    # api stuff to test server functionalities

    url(r'', include('website.urls'), name='website'),
    url(r'^admin/', include(admin.site.urls)),


)
