from collections import Counter, defaultdict
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        right = Counter(nums)
        left = defaultdict(int)

        for i, num in enumerate(nums):
            right[num] -= 1
            left[num] += 1

            if left[num] > (i+1) // 2 and right[num] > (len(nums) - i - 1) // 2:
                return i

        return -1
