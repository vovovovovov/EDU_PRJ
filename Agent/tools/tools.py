import json
import os
from langchain_community.tools.tavily_search import TavilySearchResults
'''
1.写文件
2.读文件
3.追加
4.网络搜索
'''


def _get_workdir_root():
    workdir_root = os.environ.get("WORKDIR_ROOT", './data/llm_result')
    return workdir_root

WORKDIR_ROOT = _get_workdir_root()

# 读文件
def read_file(file_name):

    if os.path.exists(file_name):
        return f"{file_name} not exist,please check file exist before read"
    with open(file_name, 'r') as f:
        return "\n".join(f.readlines())


# 追加文件
def append_file(file_name, content):
    file_name = os.path.join(WORKDIR_ROOT, file_name)
    if not os.path.exists(file_name):
        return f"{file_name} not exist,please check file"

    with open(file_name, 'a') as f:
        f.write(content)
    return "append content to file succeed"

# 写入文件
def write_to_file(file_name, content):
    pass


# 网络搜索
def search(query):
    tavily_search = TavilySearchResults(max_results=5)
    try:
        ret = tavily_search.invoke(input=query)

        """
        ret:
        [{
            "content": "",
            "url":
        }]
        """
        content_list = [obj["content"] for obj in ret]
        return "\n".join(content_list)
    except Exception as e:
        return "search error: {}".format(str(e))

tools_info = [
    # 读文件
    {
        "name" : "read_file",
        "description" : "read file from agent generate,should write file befor read",
        "args":[{
            "name" : "file_name",
            "type": "string",
            "description" : "read file name"
        }]
    },
    # 增文件
    {
        "name" : "append_file",
        "description" : "append llm content to file,should write file befor read",
        "args":[{
            "name" : "file_name",
            "type": "string",
            "description" : "append to file content"
        }]
    },
    # TODO 写文件
    {
        "name": "write_file",
        "description": "append llm content to file,should write file befor read",
        "args": [{
            "name": "file_name",
            "type": "string",
            "description": "append to file content"
        }]
    },
    # 网络搜索
    {
        "name": "search",
        "description" : "搜索引擎,进行网络搜索",
        "args":[{
            "name" : "query",
            "type": "string",
            "description" : "search query to look up"
        }]
    },
]

tools_map = {
    "read_file" : read_file,
    "append_file" : append_file,
    "write_file" : write_to_file,
    "search" : search
}

def gen_tool_desc():
    tools_desc  = []
    for idx, t in enumerate(tools_info):
        args_desc = []
        for info in t['args']:
            args_desc.append({
                "name" : info['name'],
                "description": info['description'],
                "type" : info['type'],
            })
        args_desc = json.dumps(args_desc, ensure_ascii=False)
        tool_desc = f"{idx +1}. {t['name']} : {t['description']},args: {args_desc}"
        tools_desc.append(tool_desc)
    tools_prompt = "\n".join(tools_desc)
    return tools_prompt
