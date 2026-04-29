from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        
        # pair value with index
        arr = list(enumerate(nums))  # (index, value)

        def merge_sort(enum):
            mid = len(enum) // 2
            if mid == 0:
                return enum

            left = merge_sort(enum[:mid])
            right = merge_sort(enum[mid:])

            merged = []
            i = j = 0
            right_count = 0

            while i < len(left) and j < len(right):
                if left[i][1] > right[j][1]:
                    # right[j] is smaller
                    right_count += 1
                    merged.append(right[j])
                    j += 1
                else:
                    counts[left[i][0]] += right_count
                    merged.append(left[i])
                    i += 1

            while i < len(left):
                counts[left[i][0]] += right_count
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        merge_sort(arr)
        return counts
