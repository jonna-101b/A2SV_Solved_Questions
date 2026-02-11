f
rom collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurrence = Counter(s)

        for char in t:
            if char not in occurrence or occurrence[char] == 0:
                return False

            occurrence[char] -= 1

        for char in occurrence:
            if occurrence[char]:
                return False

        return True