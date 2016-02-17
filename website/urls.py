from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from website.views import  *

admin.autodiscover()


handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.page_error'

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'loginsight_site.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^$', index, ),
                       url(r'^index', index),
                       url(r'register', register),
                       url(r'^about', about),
                       url(r'^contact', contact_us),
                       url(
                           regex=r'^login',
                           view='django.contrib.auth.views.login',
                           kwargs={'template_name': 'loginsight/login.html'}
                       ),
                       url(
                           regex=r'^$',
                           view=HomeView.as_view(),
                           name='index'
                       ),

                       url(
                           regex='^accounts/logout/$',
                           view='django.contrib.auth.views.logout',
                           kwargs={'next_page': reverse_lazy('index')}
                       ),

                       url(r'^price', price),
                       url(r'^recruitment', recruitment),
                       url(r'^landing', landingpage),
                       url(r'^checkemail', check_email),
                       url(r'^checkphone', check_phone),
                       url(r'^signupcom', signupcom),
                       url(r'^404', f404),
                       url(r'^logo', logo),
                       url(r'^ceshi', ceshi),
                       url(r'^secret$', secret_page, name='secret'),
                       )
