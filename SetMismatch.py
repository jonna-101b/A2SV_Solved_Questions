from collections import Counter
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [None, None]
        n = Counter(nums)

        for num in range(1, len(nums) + 1):
            if num not in n:
                res[1] = num
            
            elif n[num] == 2:
                res[0] = num

        return res
