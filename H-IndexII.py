from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counter = 0
        for i in range(len(citations)-1, 0, -1):
            counter += 1
            if citations[i-1] <= counter <= citations[i]:
                return counter

        counter += 1
        if counter <= citations[0]:
            return counter

        return 0 
