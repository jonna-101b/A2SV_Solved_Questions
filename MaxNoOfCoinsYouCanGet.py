from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        m = len(piles) - 2
        b = 0
        maximum = 0

        while b < m:
            maximum += piles[m]
            m -= 2
            b += 1

        return maximum
