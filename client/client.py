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
    r = requests.post(url, data={'grant_type': 'password', 'username': username, 'password':password }, headers=headers)
    print r.text
    access_token = r.json()
    print 'access_token=', access_token
    return access_token


def refresh_access_token():
    print '\n\nrefresh access token...'
    # 刷新access token
    access_token = get_access_token()
    r = requests.post(url, data={'grant_type': 'refresh_token', 'refresh_token': access_token['refresh_token']}, headers=headers)
    print r.json()
    return r.json()


if __name__ == "__main__":
    #用token来执行oauth api
    access_token = get_access_token()

    print '\n\nexcute api with token...'
    print '\n\n read groups...'
    headers = {"Authorization": access_token['token_type'] + " " + access_token['access_token']}
    r = requests.get("http://localhost:8000/api/0/groups/", headers=headers)
    print r.json()

    print '\n\n add user...'
    r = requests.post("http://localhost:8000/api/0/users/", data={'username': username, 'password': password}, headers=headers)
    print r.json()



