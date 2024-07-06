# encoding: utf-8

import uuid
import requests
from auth_util import gen_sign_headers
from pprint import pprint

# 注意替换APP_ID、APP_KEY
APP_ID = '3034087088'
APP_KEY = 'VqTRYRSlVJuFtPbb'
URI = '/translation/query/self'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'POST'

def text_translate():

    text = "I'm fine"
    data = {
        'from': 'en',
        'to': 'zh-CHS',
        'text': text,
        'app': 'test',
        'requestId': str(uuid.uuid4())
    }
    params = {}
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
    print('headers', headers)
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    url = 'https://{}{}'.format(DOMAIN, URI)

    res = requests.post(url=url, headers=headers, data=data)

    if res.status_code == 200:
        pprint(res.json())
    else:
        pprint(res.status_code, res.text)


if __name__ == '__main__':
    text_translate()