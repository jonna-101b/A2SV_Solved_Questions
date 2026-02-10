from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrence = defaultdict(int)

        for num in nums:
            occurrence[num] += 1

        elements = [[num, occurrence[num]] for num in occurrence]
        elements.sort(key = lambda x: x[1], reverse = True)

        return [elements[i][0] for i in range(k)]