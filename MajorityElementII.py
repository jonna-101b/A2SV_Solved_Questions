from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        appearance = defaultdict(int)

        for num in nums:
            appearance[num] += 1

        limit = len(nums)//3
        res = []
        for num in appearance:
            if appearance[num] > limit:
                res.append(num)

        return res