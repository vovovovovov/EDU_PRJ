from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# 测试文档
documents = [
    "AIGC创新大赛好好玩呀",
    "蓝心大模型好好玩呀",
]

# 初始化TF-IDF向量化器
vectorizer = TfidfVectorizer()

# 拟合并转换文档集合
tfidf_matrix = vectorizer.fit_transform(documents)

# 获取词汇表
feature_names = vectorizer.get_feature_names_out()

# 打印TF-IDF矩阵
for i, doc in enumerate(documents):
    print(f"Document {i + 1}:")
    # 获取当前文档的TF-IDF向量
    tfidf_vector = tfidf_matrix[i].toarray().flatten()  # 转换为numpy数组并展平
    for col in tfidf_matrix[i].nonzero()[1]:  # 获取非零元素的列索引
        print(f"  {feature_names[col]}: {tfidf_vector[col]:.4f}")

# 打印完整的TF-IDF矩阵
print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())
