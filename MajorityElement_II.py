from collections import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        new = []
        n = len(nums)
        count = Counter(nums)
        for num in count:
            if count[num] > n//3:
                new.append(num)
        return new
