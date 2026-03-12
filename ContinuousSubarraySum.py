from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0:-1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            r = prefix_sum % k

            if r in remainder:
                if abs(remainder[r] - i) >= 2:
                    return True
            else:
                remainder[r] = i
        return False
