from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        total_length = len(merged)
        if total_length % 2 == 1: 
            return merged[total_length // 2]
        else: 
            mid1, mid2 = total_length // 2 - 1, total_length // 2
            return (merged[mid1] + merged[mid2]) / 2


