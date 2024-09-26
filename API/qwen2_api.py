import json
import requests

def llm_api(question):
    data = json.dumps({"prompt": question})
    # 设置请求的URL和头部信息
    url = ""
    headers = {"Content-Type": "application/json"}  # 发送JSON数据

    # 使用POST请求发送数据，并进行流式响应
    response = requests.post(url, headers=headers, stream=True, data=data)
    return response.text

if __name__ == '__main__':
    response = llm_api("你好,介绍一下你自己")
    print(response)


# 处理流式响应，按块读取返回的数据
# for chunk in response.iter_content(chunk_size=1024, decode_unicode=True):
#     if chunk:  # 处理非空块
#         chunk = chunk.replace("data: ", "")  # 解析SSE数据流中的前缀
#         print(chunk, end='')  # 输出生成的文本



