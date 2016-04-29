# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from django.core.management.base import BaseCommand, CommandError
from oauth2_provider.models import Application
from example.models import MyApplication
from django.conf import settings
from django.contrib.auth.models import User
from website.models import UserDetail


def update_sentry_instances():
    """
    update sentry instance model from remoting aliyun ecs
    """
    # instance_list = AliyunSDK.AliyunSDK.get_instances()
    # instance_list = instance_list['Instances']['Instance']
    # sentry_list = []
    # for e in instance_list:
    #   if e['InstanceName'][:len(settings.ALIYUN_ECS_SENTRY_INSTANCE_PREFIX)] == settings.ALIYUN_ECS_SENTRY_INSTANCE_PREFIX:
    #     sentry_list.append(e)
    # for sentry_instance in sentry_list:
    #     # update sentry_instance model
    #     sentry_ipaddress = sentry_instance['PublicIpAddress']['IpAddress'][0]
    #     url_prefix = "http://%s" % (sentry_ipaddress,)
    #     se_inst = SentryInstance.objects.filter(sentry_instance_name=sentry_instance['InstanceName'])
    #     if not se_inst:
    #         sentry_instance['sentry_ipaddress'] = sentry_ipaddress
    #         client_id, client_secret = create_sentry_application(sentry_instance)
    #         SentryInstance.objects.create(sentry_instance_name=sentry_instance['InstanceName'],
    #                                       sentry_instance_url_prefix=url_prefix,
    #                                       client_id=client_id,
    #                                       client_secret=client_secret)
    pass


# create sentry oauth application record
def create_sentry_application():
    # if not sentry_instance:
    #     return
    # name = sentry_instance['InstanceName']
    # client_id = generators.generate_client_id()
    # client_secret = generators.generate_client_secret()
    # #client_id = settings.DEFALUT_SENTRY_CLIENT_ID
    # #client_secret = settings.DEFAULT_SENTRY_CLIENT_SECRET
    # print 'client-id=', client_id
    # print 'client_secret=', client_secret
    # authorization_grant_type = Application.GRANT_AUTHORIZATION_CODE
    # client_type = Application.CLIENT_PUBLIC
    # redirect_url = "http://%s/oauth/consumer/exchange/" % (sentry_instance['sentry_ipaddress'],)
    name = 'loginsight saas'
    client_id = settings.DEFALUT_SENTRY_CLIENT_ID
    client_secret = settings.DEFAULT_SENTRY_CLIENT_SECRET
    authorization_grant_type = Application.GRANT_AUTHORIZATION_CODE
    client_type = Application.CLIENT_PUBLIC
    if settings.LOGINSIGHT_DEBUG:
        redirect_url = "http://localhost/oauth/consumer/exchange/"
    else:
        redirect_url = "http://app.loginsight.cn/oauth/consumer/exchange/"

    if not MyApplication.objects.filter(name=name):
        MyApplication.objects.create(name=name,
                                     client_id=client_id,
                                     client_secret=client_secret,
                                     authorization_grant_type=authorization_grant_type,
                                     client_type=client_type,
                                     redirect_uris=redirect_url,
                                     user_id=1)
        return client_id, client_secret


def create_logagent_application():
    if not MyApplication.objects.filter(client_id=settings.LOGAGENT_CLIENT_ID):
          MyApplication.objects.create(name="logagent",
                                       client_id=settings.LOGAGENT_CLIENT_ID,
                                       client_secret=settings.LOGAGENT_CLIENT_SECRET,
                                       authorization_grant_type=Application.GRANT_PASSWORD,
                                       client_type= Application.CLIENT_CONFIDENTIAL,
                                       redirect_uris='',
                                       user_id=1)


def create_superuserdetails():
    user = User.objects.get(id=1)
    UserDetail.objects.create(
        email='tech@loginsight.cn',
        phone='18612372380',
        org_name='LogInsight',
        domain_name='loginsight.cn',
        company='loginsight',
        name=user.username,
        password=user.password,
        server_count=0,
        user_id=user.id)


class Command(BaseCommand):
     def handle(self, *args, **options):
        # 创建一个oauth provider application 给logagent
        # 更新实例数据表
        print('Initilize website ...')
        create_sentry_application()
        create_logagent_application()
        create_superuserdetails()
