class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        current = 0
        previous = 0
        maximum = 0
        found = False
        for idx, num in enumerate(nums):
            if num == 0:
                maximum = max(current + previous, maximum)
                previous = current
                current = 0
                found = True
            else:
                current += 1
        maximum = max(current + previous, maximum)
        if not found:
            return maximum - 1
        return maximum
