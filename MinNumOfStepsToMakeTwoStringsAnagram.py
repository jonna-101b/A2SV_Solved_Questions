from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_occurrence = Counter(s)
        t_occurrence = Counter(t)
        min_steps = 0

        for char in s_occurrence:
            if char in t_occurrence:
                min_steps += s_occurrence[char] - t_occurrence[char] if s_occurrence[char] > t_occurrence[char] else 0
                continue

            min_steps += s_occurrence[char]

        return min_steps
