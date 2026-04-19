from collections import Counter
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = Counter(nums)
        counter = 0
        for i in range(3):
            j = 0
            while i in freq and j < freq[i]:
                nums[counter] = i
                counter += 1
                j += 1
