from collections import Counter
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occurrence = Counter(s)
        seen = set()
        counter = 0
        sizes = []

        for char in s:
            occurrence[char] -= 1
            counter += 1

            if char not in seen:
                if occurrence[char]: seen.add(char)
            else:
                if occurrence[char] == 0: seen.remove(char)

            if not seen:
                sizes.append(counter)
                counter = 0

        if seen:
            sizes.append(counter)

        return sizes
