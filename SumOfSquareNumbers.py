class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(c ** 0.5) + 1):
            if (c - i ** 2) ** 0.5 % 1 == 0:
                return True

        return False
