#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   wechatpy.py    
@Contact :   815569735@qq.com
@License :   (C)Copyright 2017-2018, Louis-NLPR-CASIA
@Modify Time :    2020/3/7 0007 22:23
@Author :    louis
@Version :    1.0
@Description :    None
"""

# import lib
import hashlib
import static
import requests
import json
import time
import pickle


def check_signature(signature, token, timestamp, nonce):
    arg_list = [token, timestamp, nonce]
    arg_list.sort()
    tmp_sig = "".join(arg_list)
    if hashlib.sha1(tmp_sig).hexdigest() == signature:
        pass
    else:
        raise Exception


def get_token():
    time.sleep(2)
    data = {
          "grant_type": "client_credential",
          "appid": static.ID,
          "secret": static.SECRET
    }
    # get请求中参数放在params中，post放在data中，不要混淆两者
    response = requests.get(static.TOKEN_URL, params=data)
    resp_data = json.loads(response.text)
    print(resp_data)
    if "access_token" in resp_data.keys():
        with open("wechatinfo", "wb+") as f_obj:
            pickle.dump(resp_data, f_obj)
        time.sleep(resp_data['expires_in'])
    else:
        raise Exception("token 请求错误")

# 用于创建个性化的菜单，无权限。
# def create_menu():
#     with open("wechatinfo", "rb") as f_obj:
#         token = pickle.load(f_obj)["access_token"]
#     print(token)
#     data = {
#      "button": [
#          {
#           "type": "click",
#           "name": "添加事件",
#           "url": "http://47.106.235.81/addmenu"},
#          {
#             "type": "click",
#             "name": "Continue",
#             "url": "V1001_GOOD"}
#      ]}
#     response = requests.post(static.ADD_MENU + token, data=data)
#     if json.loads(response.text)["errcode"] == 0:
#         pass
#     else:
#         print(json.loads(response.text))
#         raise Exception("创建菜单失败")


if __name__ == "__main__":
    pass