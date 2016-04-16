# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: create_superuser.py
time   : 16/4/15 下午3:54  
"""


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


class Command(BaseCommand):
     def handle(self, *args, **options):
        # 创建一个oauth provider application 给logagent
        # 更新实例数据表
        pass
