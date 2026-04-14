class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pattern = [ 0 for _ in range(len(nums)) ]
        for start, end in requests:
            pattern[start] += 1
            if end+1 < len(nums):
                pattern[end+1] -= 1

        for i in range(len(pattern)):
            if i:
                pattern[i] = pattern[i-1] + pattern[i]

        pattern.sort(reverse = True)
        nums.sort(reverse = True)
        total = 0
        for i in range(len(nums)):
            total += nums[i] * pattern[i]

        return total % (10**9 + 7)
