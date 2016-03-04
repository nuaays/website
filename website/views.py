# -*- coding: utf-8 -*-
from django.shortcuts import render
import requests
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import View
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from models import UserDetail, Organization, SentryInstance
from django.conf import settings
from django.views.generic.base import TemplateView
from rest_framework import views
from django.shortcuts import render
from oauth2_provider.generators import generate_client_id, generate_client_secret
from website.vhost import VHost
from oauth2_provider.models import AccessToken
from example.models import MyApplication
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from aliyun import AliyunSDK
from website.models import Organization, SentryInstance, UserDetail, User
from oauth2_provider.compat import urlencode
import datetime
import random


def add_application(username, application_name):
    user = User.objects.get(username=username)
    if not user:
        return
    application = MyApplication(name=application_name,
                                client_id=generate_client_id(),
                                client_secret=generate_client_secret(),
                                client_type="confidential",
                                authorization_grant_type="password",
                                user=user)
    application.save()


def index(request):
    return render_to_response('loginsight/index.html', {'CLIENT_ID': settings.CLIENT_ID,
                                                        'OAUTH_TOKEN_SERVER': settings.OAUTH_TOKEN_SERVER})


class HomeView(TemplateView):
    template_name = "loginsight/index.html"

    def get_context_data(self, **kwargs):
        sentry_instance = None
        try:
            user = UserDetail.objects.get(name=self.request.user.username)
            organization = Organization.objects.get(organization_name=user.org_name)
            sentry_instance = SentryInstance.objects.get(sentry_instance_name=organization.sentry_instance)
            print sentry_instance
        except ObjectDoesNotExist:
            pass
        # sentry_instance
        # print 'org_name===', user.org_name
        # print sentry_instance
        if sentry_instance is None:
            client_id = settings.CLIENT_ID
        else:
            client_id = sentry_instance.client_id
        client_id = "ZvwRr6t?WkzuHO5htOkCjti-FHL=Ri5DsA!;6qWX"
        kwargs['CLIENT_ID'] = urlencode({'client_id': client_id})

        kwargs['OAUTH_SERVER'] = "http://localhost:8000"

        context = super(HomeView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render_to_response('loginsight/about.html')


def contact_us(request):
    return render_to_response('loginsight/contact_us.html')


def price(request):
    return render_to_response('loginsight/price.html')


def recruitment(request):
    return render_to_response('loginsight/recruitment.html')


def check_phone(request):
    print request.method
    p = request.POST.get('cellphone')
    v = UserDetail.objects.filter(phone=p)
    if len(v) == 0:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def check_email(request):
    if request.method == 'GET':
        e = request.GET.get('email')
    if request.method == 'POST':
        e = request.POST.get('email')
    v = User.objects.filter(email=e)
    if len(v) == 0:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def check_sub_domain(request):
    if request.method == 'GET':
        sub_domain_name = request.GET.get('sub_domain_name')
    if request.method == 'POST':
        sub_domain_name = request.POST.get('sub_domain_name')
    v = Organization.objects.filter(domain_name=sub_domain_name)
    if len(v) == 0:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def check_org_name(request):
    if request.method == 'GET':
        org_name = request.GET.get('companyName')
    if request.method == 'POST':
        org_name = request.POST.get('companyName')
    v = Organization.objects.filter(organization_name=org_name)
    if len(v) == 0:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def get_sentry_instance():
    pass


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        cellphone = request.POST.get('cellphone', '')
        companyName = request.POST.get('companyName', '')
        servercnt = request.POST.get('servercnt', '')
        organization_name = companyName
        sub_domain_name = request.POST.get('sub_domain', '')
        if not User.objects.filter(username=username):
            user = User(username=username,
                        email=email,
                        is_superuser=False,
                        is_staff=True,
                        is_active=True,
                        date_joined=str(datetime.datetime.now()))
            user.set_password(password)
            user.save()
            user_details = UserDetail(email=email,
                                      phone=cellphone,
                                      company=companyName,
                                      password=password,
                                      server_count=servercnt,
                                      name=username,
                                      org_name=organization_name,
                                      domain_name=sub_domain_name,
                                      user=user)

            org = None
            sentryInstance = None
            instance_list = AliyunSDK.AliyunSDK.get_instances()
            instance_list = instance_list['Instances']['Instance']
            sentry_list = []
            for e in instance_list:
                if e['InstanceName'][:len(settings.ALIYUN_ECS_SENTRY_INSTANCE_PREFIX)] == settings.ALIYUN_ECS_SENTRY_INSTANCE_PREFIX:
                    sentry_list.append(e)
            print 'sentry instance count: ', len(sentry_list)
            sentry_count = len(sentry_list)
            sentry_index = random.randint(0, sentry_count-1)
            sentry_instance = sentry_list[sentry_index]
            # create organization
            org_list = Organization.objects.filter(sentry_instance=sentry_instance['InstanceName'])
            while len(org_list) >= settings.MAX_SENTRY_INSTANCE_COUNT:
                sentry_index = random.randint(0, sentry_count-1)
                sentry_instance = sentry_list[sentry_index]
                org_list = Organization.objects.filter(sentry_instance=sentry_instance['InstanceName'])

            # update sentry_instance model
            sentry_ipaddress = sentry_instance['PublicIpAddress']['IpAddress'][0]
            print 'ipaddress = ', sentry_ipaddress
            url_prefix = "http://%s:%s" % (sentry_ipaddress, settings.SENTRY_DEFALUT_PORT)
            se_inst = SentryInstance.objects.filter(sentry_instance_name=sentry_instance['InstanceName'])
            if not se_inst:
                print 'sentry_instance_name = ', sentry_instance['InstanceName']
                sentryInstance = SentryInstance.objects.create(sentry_instance_name=sentry_instance['InstanceName'],
                                                sentry_instance_url_prefix=url_prefix)

            domain_name = sub_domain_name + settings.DEFAULT_SUB_DOMAIN_SUFFIX
            if not (Organization.objects.filter(organization_name=organization_name)
                and Organization.objects.filter(sub_domain_name=domain_name)):
                org = Organization(organization_name=organization_name,
                                   domain_name=sub_domain_name + settings.DEFAULT_SUB_DOMAIN_SUFFIX,
                                   sentry_instance=sentry_instance['InstanceName'])
            else:
                return render_to_response("loginsight/500.html")

            # save to database
            user_details.save()
            org.save()
            # add nginx vhost conf
            VHost.addVhostConf(domain=domain_name, organization=organization_name, sentry_url=url_prefix)
            VHost.reload_nginx()

            # add domain record for Aliyun Wan network
            resp = AliyunSDK.AliyunSDK.add_domain_record(domain_name=settings.OFFICIAL_DOMAIN_NAME,
                                                         RR=domain_name,
                                                         Type="A",
                                                         Value=sentry_ipaddress)
            return render_to_response("loginsight/signup-com.html")

        else:
            return render_to_response('loginsight/signup-infor.html',  context_instance=RequestContext(request))
    c = {}
    c.update(csrf(request))
    return render_to_response("loginsight/signup-infor.html", c)


def landingpage(request):
    return render_to_response("loginsight/landing-page.html")


def signupcom(request):
    return render_to_response("loginsight/signup-com.html")

def python(request):
    return render_to_response("loginsight/landing-python.html")

def f404(request):
    return render_to_response("loginsight/404.html")

def logo(request):
    return render_to_response("loginsight/logo.html")

def ceshi(request):
    return render_to_response("loginsight/ceshi.html")

def page_not_found(request):
    return render_to_response('loginsight/404.html')

def page_error(request):
    return render_to_response('loginsight/500.html')

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

@login_required()
def secret_page(request, *args, **kwargs):
    print 'hello world'
    return HttpResponse('Secret contents!', status=200)

@login_required()
def validate_accesstoken(request):
    if request.method == 'POST':
        print 'FFF=', request.POST
        access_token = request.POST.get('access_token', '')
        t = AccessToken.objects.filter(token=access_token)
        if t:
            return HttpResponse(True)
        return HttpResponse(False)
