import uuid
import time
import requests
from auth_util import gen_sign_headers
from pprint import pprint
import base64
import json

# 替换APP_ID、APP_KEY
APP_ID = '3034087088'
APP_KEY = 'VqTRYRSlVJuFtPbb'
DOMAIN = 'api-ai.vivo.com.cn'



'''
    :func 对话功能实现
    :params my_prompt 提示词
    
    :return None

'''
def sync_vivogpt(my_prompt):
    URI = '/vivogpt/completions'   # 指定URI
    METHOD = 'POST'  # 对话使用的是post

    params = {
        'requestId': str(uuid.uuid4())
    }
    print('requestId:', params['requestId'])

    data = {
        'prompt': my_prompt,
        'model': 'vivo-BlueLM-TB',
        'sessionId': str(uuid.uuid4()),
        'extra': {
            'temperature': 0.9
        }
    }
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
    headers['Content-Type'] = 'application/json'

    start_time = time.time()
    url = 'https://{}{}'.format(DOMAIN, URI)
    response = requests.post(url, json=data, headers=headers, params=params)

    if response.status_code == 200:
        res_obj = response.json()
        pprint(f'response:{res_obj}')
        if res_obj['code'] == 0 and res_obj.get('data'):
            content = res_obj['data']['content']
            print(f'final content:\n{content}')
    else:
        print(response.status_code, response.text)
    end_time = time.time()
    timecost = end_time - start_time
    print('请求耗时: %.2f秒' % timecost)


'''
    :func 向量化
    

'''
def embedding():
    URI = '/embedding-model-api/predict/batch'
    METHOD = 'POST'

    params = {}
    post_data = {
        "model_name": "m3e-base",
        "sentences": ["豫章故郡，洪都新府", "星分翼轸，地接衡庐"]
    }
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)

    url = 'https://{}{}'.format(DOMAIN, URI)
    response = requests.post(url, json=post_data, headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code, response.text)

def ocr_test(pic_file):
    URI = '/ocr/general_recognition'
    METHOD = 'POST'

    picture = pic_file
    with open(picture, "rb") as f:
        b_image = f.read()
    image = base64.b64encode(b_image).decode("utf-8")
    post_data = {"image": image, "pos": 2, "businessid": "1990173156ceb8a09eee80c293135279"}
    params = {}
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)

    url = 'http://{}{}'.format(DOMAIN, URI)
    response = requests.post(url, data=post_data, headers=headers)
    if response.status_code == 200:
        pprint(response.json())
    else:
        pprint(response.status_code, response.text)

# api测试
if __name__ == '__main__':
    sync_vivogpt("讲一个故事")
    # embedding()
    # ocr_test("data/img.png")