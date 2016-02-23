#-*- coding: utf-8 -*
'''
Author:         wanghe 
Email:          wangh@loginsight.cn
Author website: 
 
File: client.py
Create Date: 2016-02-17 20:47:01
''' 

import base64
import requests
from flask.ext.script import Manager, Command

# 设置CLIENT_ID 和 CLIENT_SECRET 
CLIENT_ID="6Ft0BOkiVfi74D.hiSX-OK=uBlhy7k=Mt2u=DsOa"
CLIENT_SECRET="XqzcrIU@F4L-rXiF7K=2UlzrPh50KRCMojr_Ka4!:=v!yK;UOc0dLI8Ky5yzXQGTqM6pr_YGx@-U-?xeKVRRApuxxZGCJDa1x=;Of!sUmrOPa3hPtN!ky;01UX@CVnM7"

# 用户名和密码
username='hello10'
password = '123qwe'
url = "http://localhost:8000/o/token/"
headers = {"Authorization": "Basic " + base64.b64encode(CLIENT_ID + ":" + CLIENT_SECRET)}


def get_access_token():
    # 请求oauth access token
    print '\n\nget access token ...'
    r = requests.post(url, data={'grant_type': 'password', 'username': username, 'password':password, 'scope': 'read'}, headers=headers)
    print r.text
    access_token = r.json()
    return access_token


def refresh_access_token():
    print '\n\nrefresh access token...'
    # 刷新access token
    token = get_access_token()
    headers = {"Authorization": "Basic " + base64.b64encode(CLIENT_ID + ":" + CLIENT_SECRET)}
    r = requests.post(url, data={'grant_type': 'refresh_token', 'refresh_token': token['refresh_token']}, headers=headers)
    token = r.json()
    return token

if __name__ == "__main__":
    access_token = get_access_token()
    headers = {"Authorization": access_token['token_type'] + " " + access_token['access_token']}

    r = requests.get(url="http://localhost:8000/api/0/hello", headers=headers)
    print r.text

    r = requests.get(url="http://localhost:8000/secret", headers=headers)
    print r.text

    r = requests.get(url="http://localhost:8000/")
    # 获取sentry 实例
    r = requests.get(url="http://localhost:8000/api/0/hosts", headers=headers)
    print r.json()
    sentry_instance = r.json()
    # 向sentry 实例注册主机
    data = {'host_name': 'host111', 'host_type': 'web111', 'system': 'linux', 'distver': '1.0', 'mac_addr': "ff-cc-cd-20-21-21" }
    SENTRY_URL_PREFIX = "http://localhost:9000"
    # r = requests.post(url=sentry_instance['sentry_instancce_url_prefix'] + "/api/0/agent/hosts", data=data, headers=headers )
    r = requests.post(url=SENTRY_URL_PREFIX + "/api/0/agent/hosts", data=data, headers=headers )
    print r.json()
    data = {'match_name': '^ff/aaafj/cc/aa/ccccc', 'stream_key': 'xx2222xxxxx', 'host_key': 'ed141f34521c9422eea23abb202beeee', 'alias_name': 'fff'}
    r = requests.post(url=SENTRY_URL_PREFIX+"/api/0/agent/streams", data=data, headers=headers)
    print r.text
    # print r.json()
