from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_mod = 0
        remainder_freq = {0: 1}

        for num in nums:
            prefix_mod = (prefix_mod + num) % k

            if prefix_mod < 0:
                prefix_mod += k

            count += remainder_freq.get(prefix_mod, 0)

            remainder_freq[prefix_mod] = remainder_freq.get(prefix_mod, 0) + 1

        return count
