class Solution:
    def squareSum(self, num: int) -> int:
        number = str(num)
        total = 0
        for digit in number:
            total += int(digit) ** 2

        return total

    def isHappy(self, n: int) -> bool:
        occurred = set()

        while n != 1 and n not in occurred:
            occurred.add(n)
            n = self.squareSum(n)

        return n == 1