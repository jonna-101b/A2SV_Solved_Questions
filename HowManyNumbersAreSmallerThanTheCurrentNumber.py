from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_nums = nums.copy()
        new_nums.sort()
        counter = dict()
        i = 0
        j = 0
        print(nums)

        for num in new_nums:
            if num not in counter:
                i += j
                counter[num] = i
                i += 1
                j = 0

            else:
                j += 1

        for i in range(len(nums)):
            nums[i] = counter[nums[i]]

        return nums
