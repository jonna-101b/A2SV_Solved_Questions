class Solution:
    def minimumReplacement(self, nums):
        ops = 0
        max_allowed = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= max_allowed:
                max_allowed = nums[i]
            else:
                k = (nums[i] + max_allowed - 1) // max_allowed  
                ops += k - 1
                max_allowed = nums[i] // k
        
        return ops
