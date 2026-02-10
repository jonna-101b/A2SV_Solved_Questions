from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        occurrence = dict()
        for i in range(len(nums)):
            if nums[i] in occurrence:
                occurrence[nums[i]] += [i]
                continue

            occurrence[nums[i]] = [i]

        for i in range(len(nums)):
            reminder = target - nums[i]
            if reminder in occurrence:
                for index in occurrence[reminder]:
                    if index != i:
                        return [i, index]

        return []