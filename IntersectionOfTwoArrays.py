from collections import Counter
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_occurrence = Counter(nums1)
        nums2_occurrence = Counter(nums2)
        intersection = []

        for num in nums1_occurrence:
            if num in nums2_occurrence:
                intersection.append(num)

        return intersection
