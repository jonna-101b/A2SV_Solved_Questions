class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        count = 0
        current_sum = 0
        seen = {0: 1}  

        for num in nums:
            current_sum += num

            if current_sum - goal in seen:
                count += seen[current_sum - goal]

            seen[current_sum] = seen.get(current_sum, 0) + 1

        return count
