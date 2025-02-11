import math
import re
from collections import Counter


class TextStatistics:
    def __init__(self, text: str):
        self.text = text.lower()
        self.words = re.findall(r'\w+', self.text)
        self.total_words = len(self.words)
        self.documents = [line for line in self.text.splitlines() if line.strip()]
        self.num_documents = len(self.documents) if self.documents else 1

    def compute_tf(self) -> dict:
        counts = Counter(self.words)
        return dict(counts)

    def compute_df(self) -> dict:
        df = {}
        for doc in self.documents:
            unique_words = set(re.findall(r'\w+', doc))
            for word in unique_words:
                df[word] = df.get(word, 0) + 1
        return df

    def compute_idf(self) -> dict:
        df = self.compute_df()
        idf = {}
        for word in set(self.words):
            idf[word] = math.log10(self.num_documents / df.get(word, 1))
        return idf
