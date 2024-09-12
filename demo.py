# 基于langchain 的教育领域大模型基本demo

from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS

from langchain.embeddings import HuggingFaceEmbeddings
from pprint import pprint

# vivio 蓝心 70B 大模型
from API.BlueLM_api import *








# 大模型处理
def test_demo(my_prompt):
    # 数据加载
    loader = PyPDFLoader(r"D:\PycharmProject_new\EDU_PRJ\Data_Process\data\信息技术与数据挖掘-2021-8-16.pdf")
    pages = loader.load_and_split()

    # 第一页
    page_one = pages[0].page_content

    embedding = HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5")
    # 向量库
    faiss_index = FAISS.from_documents(pages, embedding)
    # 运用milvus向量库

    # 向量相似度检索
    docs = faiss_index.similarity_search(my_prompt, k=2)

    str_list = []
    for doc in docs:
        print(str(doc.metadata["page"]) + ":", doc.page_content[:300])
        str_list.append(doc.page_content)

    response  = sync_vivogpt(my_prompt,systemPrompt="你是教学小助手", temperature=0.7)

    return response + "\n" + str(str_list[0]) + "\n" + str(str_list[1])














