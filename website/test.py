# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""
import requests
# user register

data = {
    'username': 'h2',
    'email': 'h2@qq.com',
    'password': '123qwe',
    'cellphone': '111111111',
    'companyName': 'h2',
    'servercnt': 1,
    'sub_domain':  'h2.loginsight.cn'
}
r = requests.post("http://localhost:8000/register", data=data)
print r.text