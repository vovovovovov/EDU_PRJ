#!/usr/bin/env python
# encoding: utf-8

import requests
import base64
import json
from auth_util import gen_sign_headers
from pprint import pprint

# 请注意替换APP_ID、APP_KEY
APP_ID = '3034087088'
APP_KEY = 'VqTRYRSlVJuFtPbb'
URI = '/api/v1/task_progress'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'GET'

def submit():

    params = {}
    data = {
    'height': 768,
    'width': 576,
    'prompt': '一只梵高画的猫',
    'styleConfig': '55c682d5eeca50d4806fd1cba3628781'
    }

    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
    headers['Content-Type'] = 'application/json'

    url = 'http://{}{}'.format(DOMAIN, URI)
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        pprint(response.json())
    else:
        pprint(response.status_code, response.text)

def progress():
   params = {
       # 注意替换为提交作画任务时返回的task_id
       'task_id': '1f8c25a7db2a5173bef9b2bee65d3879'
   }
   headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)

   uri_params = ''
   for key, value in params.items():
       uri_params = uri_params + key + '=' + value + '&'
   uri_params = uri_params[:-1]

   url = 'http://{}{}?{}'.format(DOMAIN, URI, uri_params)
   print('url:', url)
   response = requests.get(url, headers=headers)
   if response.status_code == 200:
       print(response.json())
   else:
       print(response.status_code, response.text)

if __name__ == '__main__':
   progress()

# if __name__ == '__main__':
#     submit()