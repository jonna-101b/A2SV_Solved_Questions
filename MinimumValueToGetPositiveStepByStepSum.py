from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        startValue = 0

        for num in nums:
            prefix_sum += num
            startValue = max(startValue, (prefix_sum - 1) * -1)

        return max(startValue, (prefix_sum - 1) * -1, 1)
