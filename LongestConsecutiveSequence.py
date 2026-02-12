from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = list(set(nums))
        new_nums.sort()
        max_length = 0
        consecutive = 0
        last_num = None
        
        for num in new_nums:
            if last_num is None:
                consecutive = 1 
            elif num - last_num == 1:
                consecutive += 1
            else:
                consecutive = 1

            max_length = max(max_length, consecutive)
            last_num = num

        return max_length
