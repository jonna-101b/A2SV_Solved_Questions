class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def valid(a: str, b: str, start: int) -> bool:
            while start < n:
                c = str(int(a) + int(b))
                if not num.startswith(c, start):
                    return False
                start += len(c)
                a, b = b, c
            return True

        for i in range(1, n):
            for j in range(i + 1, n):
                a, b = num[:i], num[i:j]
                if (a[0] == '0' and len(a) > 1) or (b[0] == '0' and len(b) > 1):
                    continue

                if valid(a, b, j):
                    return True

        return False
