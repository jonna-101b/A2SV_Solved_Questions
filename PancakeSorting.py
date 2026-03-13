from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)

        for size in range(n, 1, -1):
            # Find index of current largest value (size)
            max_idx = arr.index(size)

            # If already in correct position, skip
            if max_idx == size - 1:
                continue

     
            if max_idx != 0:
                arr[:max_idx+1] = reversed(arr[:max_idx+1])
                res.append(max_idx + 1)

            
            arr[:size] = reversed(arr[:size])
            res.append(size)

        return res
