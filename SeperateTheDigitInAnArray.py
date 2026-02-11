from math import log10, floor
from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                answer.append(0)
                continue

            digit = floor(log10(num)) + 1
            while digit:
                number = num // pow(10, digit - 1)
                answer.append(number)
                num -= (number * pow(10, digit - 1))
                digit -= 1

        return answer