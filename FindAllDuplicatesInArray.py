from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        appeared = set()
        duplicates = []

        for num in nums:
            if num in appeared:
                duplicates.append(num)
                continue

            appeared.add(num)

        return duplicates