from sortedcontainers import SortedList
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        check = set(nums1)
        index_store = {}
        unsolved = SortedList(key = lambda x: -x)

        for num in nums2:
            if num in check:
                index_store[num] = -1
                unsolved.add(num)

            i = len(unsolved) - 1
            while unsolved and num > unsolved[i]:
                    index_store[unsolved.pop()] = num
                    i -= 1


        ans = [index_store[num] for num in nums1]
        
        return ans
