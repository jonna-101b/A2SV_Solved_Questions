from collections import Counter

class Solution:
    def checkConditions(self, last_digit: str, curr_digit: str, occurrence: dict[str: int]) -> bool:
        return last_digit and last_digit != curr_digit and int(last_digit) == occurrence[last_digit] and int(curr_digit) == occurrence[curr_digit]

    def findValidPair(self, s: str) -> str:
        occurrence = Counter(s)
        last_digit = None

        for digit in s:
            if self.checkConditions(last_digit, digit, occurrence):
                return last_digit + digit

            last_digit = digit

        return ""
