from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        without_zero = 1
        
        for num in nums:
            product *= num

            if num == 0:
                zero_count += 1
            else:
                without_zero *= num

        answer = []
        for num in nums:
            if num:
                answer.append(product // num)
            else:
                if zero_count > 1:
                    answer.append(0)
                else:
                    answer.append(without_zero)

        return answer
