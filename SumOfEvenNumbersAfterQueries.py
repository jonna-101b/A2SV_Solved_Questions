from typing import List

class Solution:
    def findEvenSum(self, nums: List[int]) -> int:
        total_sum = 0
        for num in nums:
            total_sum += num if num % 2 == 0 else 0

        return total_sum

    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        even_sum = self.findEvenSum(nums)

        for val, index in queries:
            even_sum -= nums[index] if nums[index] % 2 == 0 else 0
            nums[index] += val
            even_sum += nums[index] if nums[index] % 2 == 0 else 0 
            res.append(even_sum)

        return res