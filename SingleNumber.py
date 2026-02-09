from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        appearance = dict()

        for num in nums:
            if num in appearance:
                appearance[num] += 1
                continue

            appearance[num] = 1

        for num in appearance:
            if appearance[num] == 1:
                return num