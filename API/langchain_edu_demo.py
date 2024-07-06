# 基于langchain 的教育领域大模型基本demo

from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS

from langchain.embeddings import HuggingFaceEmbeddings
from pprint import pprint

# vivio 蓝心 70B 大模型
from BlueLM_api import sync_vivogpt

# 数据加载
loader = PyPDFLoader(r"D:\PycharmProject_new\BlueLM\BlueLM_technical_report.pdf")
pages = loader.load_and_split()

# 第一页
page_one = pages[0].page_content


# embedding 模型定义
embedding = HuggingFaceEmbeddings(model_name=r"C:\Users\23941\.cache\huggingface\hub\models--shibing624--text2vec-base-chinese\snapshots\4aedd18edec668a8e716d95eda081aba8151ffd3")

# 向量库
faiss_index = FAISS.from_documents(pages, embedding)

# 向量相似度检索
docs = faiss_index.similarity_search("What is BlueLM?", k=2)

str_list = []
for doc in docs:
    print(str(doc.metadata["page"]) + ":", doc.page_content[:300])
    str_list.append(doc.page_content[:300])


# Prompt 编写
my_prompt = "What is BlueLM?, based on the information follwos :" + str_list[0] + str_list[1] + "full details please"
print("*******************************************")
print(my_prompt)
print("*******************************************")

# 大模型处理

sync_vivogpt(my_prompt)











