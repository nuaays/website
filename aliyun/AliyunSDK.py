# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""
import requests
import datetime
import urllib
import aliyun.api
from django.conf import settings


class AliyunSDK:
    access_key_id = settings.ALIYUN_ACCESS_KEY_ID
    access_key_secret = settings.ALIYUN_ACCESS_KEY_SECRET
    aliyun.setDefaultAppInfo(access_key_id, access_key_secret)

    @staticmethod
    def get_instances_status():
        a = aliyun.api.Ecs20140526DescribeInstanceStatusRequest()
        a.PageNumber = 1
        a.PageSize = 10
        a.RegionId = settings.ALIYUN_ECS_REGIONID
        f = a.getResponse()
        return f

    @staticmethod
    def add_domain_record(**kwargs):
        a = aliyun.api.Dns20150109AddDomainRecordRequest()
        a.DomainName = kwargs['domain_name']
        a.RR = kwargs['RR']
        a.Type = kwargs['Type']
        a.Value = kwargs['Value']
        f = a.getResponse()
        return f

    @staticmethod
    def get_instances():
        a = aliyun.api.Ecs20140526DescribeInstancesRequest()
        a.RegionId = settings.ALIYUN_ECS_REGIONID
        f = a.getResponse()
        return f