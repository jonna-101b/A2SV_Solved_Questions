from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, dxn in shifts:
            val = 1 if dxn == 1 else -1
            diff[start] += val
            diff[end + 1] -= val

        # prefix sum to get actual shifts
        for i in range(1, n):
            diff[i] += diff[i - 1]

        res = []
        for i in range(n):
            net = (ord(s[i]) - ord('a') + diff[i]) % 26
            res.append(chr(ord('a') + net))

        return "".join(res)
