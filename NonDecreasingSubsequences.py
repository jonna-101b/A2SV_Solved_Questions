class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsequence = []

        def backtrack(i, path):
            if len(path) >= 2:
                subsequence.append(path[:])

            seen = set()
            for j in range(i, n):
                if nums[j] in seen or (path and nums[j] < path[-1]):
                    continue
                seen.add(nums[j])

                path.append(nums[j])
                backtrack(j+1, path)
                path.pop()

        backtrack(0, [])

        return subsequence
