from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = None

        for string in strs:
            if prefix == None:
                prefix = string
                continue

            i = 0
            while i < min(len(string), len(prefix)) and string[i] == prefix[i]:
                i += 1

            prefix = prefix[:i]

        return prefix