# -*- coding: utf-8 -*-
from django.shortcuts import render
import requests
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.conf import settings
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from models import UserDetail
from django.conf import settings
from django.views.generic.base import TemplateView
from oauth2_provider.generators import generate_client_id, generate_client_secret
from oauth2_provider.models import AccessToken
from example.models import MyApplication
from django.template import RequestContext
from oauth2_provider.compat import urlencode
import datetime


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
        client_id = settings.DEFALUT_SENTRY_CLIENT_ID
        kwargs['CLIENT_ID'] = urlencode({'client_id': client_id})
        kwargs['OAUTH_SERVER'] = settings.OAUTH_SERVER
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
    pass


def check_org_name(request):
    if request.method == 'GET':
        org = request.GET.get('org_name')
    v = UserDetail.objects.filter('companyName')
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
        servercnt = request.POST.get('servercnt', 0)
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
            user_details.save()
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

def product(request):
    return render_to_response("loginsight/product.html")

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
