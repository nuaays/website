# -*- coding: utf-8 -*-
from django.shortcuts import render
import requests
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import View
from django.contrib.auth.models import User
from models import UserDetail
import datetime

def index(request):
    return render_to_response('loginsight/index.html')


def about(request):
    return render_to_response('loginsight/about.html')


def contact_us(request):
    return render_to_response('loginsight/contact_us.html')


def price(request):
    return render_to_response('loginsight/price.html')


def recruitment(request):
    return render_to_response('loginsight/recruitment.html')


def login(request):
    return render_to_response('loginsight/login.html', )


def check_phone(request):
    p = request.POST.get('cellphone')
    v = UserDetail.objects.filter(phone=p)
    if len(v) == 0:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def check_email(request):
    e = request.POST.get('email')
    v = User.objects.filter(email=e)
    if len(v) == 0:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def register(request):
    if request.method == 'POST':
        name = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        cellphone = request.POST.get('cellphone', '')
        companyName = request.POST.get('companyName', '')
        servercnt = request.POST.get('servercnt', '')

        if not User.objects.filter(username=name):
            user = User(username=name,
                        email=email,
                        is_superuser=False,
                        is_staff=True,
                        is_active=True,
                        date_joined=str(datetime.datetime.now()))

            user_details = UserDetail(email=email,
                                      phone=cellphone,
                                      company=companyName,
                                      password=password,
                                      server_count=servercnt,
                                      name=name,
                                      user=user)

            user.save()
            user_details.save()
            return render_to_response("loginsight/signup-com.html")

        else:
             return render_to_response('loginsight/signup-infor.html', {'msg': '账户名已存在'})

    return render_to_response("loginsight/signup-infor.html")


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