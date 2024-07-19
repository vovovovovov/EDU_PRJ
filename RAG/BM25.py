import numpy as np
from collections import Counter
from math import log

class BM25:
    def __init__(self, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.doc_lengths = []
        self.avgdl = 0
        self.idf = {}
        self.docs = []

    def fit(self, documents):
        self.docs = documents
        self.doc_lengths = [len(doc.split()) for doc in documents]
        self.avgdl = np.mean(self.doc_lengths)
        self._compute_idf()

    def _compute_idf(self):
        N = len(self.docs)
        doc_freq = {}
        for doc in self.docs:
            terms = set(doc.split())
            for term in terms:
                if term not in doc_freq:
                    doc_freq[term] = 0
                doc_freq[term] += 1

        self.idf = {
            term: log((N - df + 0.5) / (df + 0.5) + 1.0)
            for term, df in doc_freq.items()
        }

    def score(self, query, doc):
        score = 0.0
        doc_terms = Counter(doc.split())
        doc_length = len(doc.split())

        for term in query.split():
            tf = doc_terms.get(term, 0)
            idf = self.idf.get(term, 0)
            print(f"Term: {term}, TF: {tf}, IDF: {idf}")  # Debug output
            score += idf * (tf * (self.k1 + 1)) / (tf + self.k1 * (1 - self.b + self.b * (doc_length / self.avgdl)))

        return score

# 示例文档集合
documents = [
    "vivo蓝心70b大模型",
    "AIGC创新大赛好好玩呀",
    "蓝心大模型好好玩呀",
]

# 初始化BM25模型并训练
bm25 = BM25(k1=1.5, b=0.75)
bm25.fit(documents)

# 查询
query = "蓝心大模型"

# 打印每个文档的BM25分数
for i, doc in enumerate(documents):
    print(f"Document {i + 1}: BM25 Score = {bm25.score(query, doc):.4f}")
