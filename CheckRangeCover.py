from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key = lambda x: x[0])
        interval = [False for i in range(left, right+1)]
        last = left

        for item in ranges:
            if item[0] <= last <= item[1]:
                for i in range(last, min(right, item[1]) + 1):
                    interval[i - left] = True
                    last = i + 1

        return all(interval)