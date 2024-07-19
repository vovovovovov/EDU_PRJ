import numpy as np
from collections import Counter
from math import log


def compute_probability_distribution(doc):
    total_terms = len(doc.split())
    term_count = Counter(doc.split())
    return {term: count / total_terms for term, count in term_count.items()}


def kl_divergence(p, q):
    """计算Kullback-Leibler散度"""
    divergence = 0.0
    for term in p:
        if term in q:
            divergence += p[term] * log(p[term] / q[term])
        else:
            divergence += p[term] * log(p[term] / 1e-10)  # 避免log(0)
    return divergence


def knk_score(doc1, doc2):
    """计算文档之间的KNK分数"""
    p = compute_probability_distribution(doc1)
    q = compute_probability_distribution(doc2)

    kl_pq = kl_divergence(p, q)
    kl_qp = kl_divergence(q, p)

    return (kl_pq + kl_qp) / 2


# 示例文档集合
documents = [
    "vivo蓝心70b大模型",
    "AIGC创新大赛好好玩呀",
    "蓝心大模型好好玩呀",
]

# 计算每对文档之间的KNK分数
for i in range(len(documents)):
    for j in range(i + 1, len(documents)):
        score = knk_score(documents[i], documents[j])
        print(f"KNK Score between Document {i + 1} and Document {j + 1}: {score:.4f}")
