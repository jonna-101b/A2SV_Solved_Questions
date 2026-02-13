from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_occurrence = Counter(ransomNote)
        mg_occurrence = Counter(magazine)

        for char in rn_occurrence:
            if char not in mg_occurrence or rn_occurrence[char] > mg_occurrence[char]:
                return False

        return True
