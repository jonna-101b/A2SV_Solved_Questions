class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        _max = deque()
        _min = deque()  
        ans = 0
        left = 0
        
        for right in range(len(nums)):
    
            while _max and nums[_max[-1]] <= nums[right]:
                _max.pop()
            while _min and nums[_min[-1]] >= nums[right]:
                _min.pop()
            
            _max.append(right)
            _min.append(right)
            
 
            while nums[_max[0]] - nums[_min[0]] > limit:
                left += 1
                if _max[0] < left:
                    _max.popleft()
                if _min[0] < left:
                    _min.popleft()
            
         
            ans = max(ans, right - left + 1)
        
        return ans
