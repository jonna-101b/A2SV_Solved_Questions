from typing import List

class Solution:
    def intToRoman(self, num: int) -> str:
        digits = {1: ["I", "V"], 2: ["X", "L"], 3: ["C", "D"], 4: ["M", "Z"]}
        num = str(num)
        roman_eq = []

        for i in range(len(num)):
            curr_digit = len(num) - i
            digit = int(num[i])

            if digit < 5:
                if digit == 4:
                    roman_eq.append(digits[curr_digit][0] + digits[curr_digit][1])
                else:
                    roman_eq.append(digits[curr_digit][0] * digit)

            else:
                if digit == 9:
                    roman_eq.append(digits[curr_digit][0] + digits[curr_digit + 1][0])
                else:
                    roman_eq.append(digits[curr_digit][1] + digits[curr_digit][0] * (digit - 5))

        return "".join(roman_eq)