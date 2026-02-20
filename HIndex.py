from collections import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        h = 0
        for i,n in enumerate(citations):
            if n >= i + 1:
                h += 1
            else:
                break
        return h
