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


# TODO 多轮对话功能还未添加
'''
    :func 对话功能实现（同步接口，一次性返回）
    
    输入参数
    :param  my_prompt 问题
    :param  systemPrompt  设定的回答模板 （在这个上面做文章）
    :param  temperature  采样温度，控制输出的随机性，必须为正数取值范围是：(0.0,1.0]，
                         不能等于 0,值越大，会使输出更随机，更具创造性；值越小，输出会更加稳定或确定
    :param  multi_turn_talk  是否进行多轮对话,默认为False
    
    返回参数
    :return content 结果

'''
def sync_vivogpt(my_prompt, systemPrompt, temperature,multi_turn_talk=False):
    URI = '/vivogpt/completions'   # 指定URI
    METHOD = 'POST'  # 对话使用的是post

    params = {
        'requestId': str(uuid.uuid4())
    }
    print('requestId:', params['requestId'])

    data = {
        'prompt': my_prompt,  # 单轮对话
        # 'message': message   #多轮对话
        'model': 'vivo-BlueLM-TB',
        'sessionId': str(uuid.uuid4()),
        'systemPrompt': systemPrompt,
        'extra': {
            'temperature': temperature
        }
    }
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
    headers['Content-Type'] = 'application/json'

    start_time = time.time()
    url = 'https://{}{}'.format(DOMAIN, URI)
    response = requests.post(url, json=data, headers=headers, params=params)
    content = None
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
    return content


# TODO embedding接口优化
'''
    :func 向量化
    输入参数:
        sentences : 要向量化的句子  (List数据类型)
    返回参数:
        向量化后的句子 (列表数据类型)

'''
def embedding(sentences):
    URI = '/embedding-model-api/predict/batch'
    METHOD = 'POST'

    params = {}
    post_data = {
        "model_name": "m3e-base",
        "sentences": sentences
    }
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)

    url = 'https://{}{}'.format(DOMAIN, URI)
    response = requests.post(url, json=post_data, headers=headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()['data']
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
    # systemPrompt = '你的中文名字叫xx助手，当回复问题时需要回复你的名字时，中文名必须回复xx助手，此外回复和你的名字相关的问题时，也需要给出和你的名字对应的合理回复。'
    # content = sync_vivogpt("讲一个故事",systemPrompt = systemPrompt,temperature= 0.9)
    print("************************************")
    # list = ["你好"]
    # data = embedding(list)
    # print(data)
    # embedding()
    # ocr_test("data/img.png")