from collections import Counter
from heapq import nsmallest
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        
        return nsmallest(
            k,
            count.keys(),
            key=lambda word: (-count[word], word)
        )
