from collections import Counter
from typing import List

class Solution:
    def checkOriginal(self, original: List[int], changed: List[int]) -> List[int]:
        if len(changed) / 2 != len(original):
            return []

        og_changed = []
        for num in original:
            og_changed.append(num)
            og_changed.append(num * 2)

        og_changed.sort()
        changed.sort()
        for i in range(len(og_changed)):
            if og_changed[i] != changed[i]:
                return []

        return original if og_changed == changed else []

    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        changed.sort()
        occurred = Counter(changed)
        original = []
        zero_occurred = False

        for num in changed:
            if num == 0:
                if zero_occurred:
                    zero_occurred = False

                elif occurred[0] > 1:
                    occurred[0] -= 2
                    original.append(0)
                    zero_occurred = True

                else:
                    return []

            elif num * 2 in occurred:
                if occurred[num]:
                    occurred[num] -= 1
                    occurred[num * 2] -= 1
                    original.append(num)


        return self.checkOriginal(original, changed)
