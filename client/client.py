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
CLIENT_ID="QIC2k0tpZB_.yjgfC9-ks0WGDauRnmaM7F.gbzK9"
CLIENT_SECRET="ZnFc8jL?uqnUxI6!;ZjCfhwKS@H0RtZV2=Iu;iHbMqtK5a@XcfQ3@3oD2FZh?tvahz?Qohz-Vnb2ECaNlJ4r_vwb@hXig;QNjydwAE4f5qx7L2D7BbXhZMVsdT?sNJQM"

# 用户名和密码
username='wanghe'
password = '123'
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
    print 'headers = ', headers
    # r = requests.get(url="http://localhost:8000/api/0/groups", headers=headers)
    # print r.text
    r = requests.post(url="http://localhost:9000/api/0/agent/hosts",
                      data={'host_name': '1xx2212rrrx', 'host_type':'xxx222rr', 'distver': '1.0', 'system': 'linux'},
                      headers=headers)
    print r

    r = requests.get(url="http://localhost:8000/api/0/hello", headers=headers)
    print r.text

    #
    # r = requests.get(url="http://localhost:9000/api/0/agent/hello", headers=headers)
    # # r = requests.get(url="http://localhost:8000/secret", headers=headers)
    # print r.json()
    #
    # r = requests.get(url="http://localhost:8000/api/0/access_token", headers=headers)
    # print r, r.text
    #
    # r = requests.get(url="http://localhost:9000/api/0/accesstoken", headers=headers)
    # print r, r.text
