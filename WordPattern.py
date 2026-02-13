class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        occurrence = dict()
        values = dict()
        s = s.split()
        if len(pattern) != len(s): return False

        for i in range(len(pattern)):
            if pattern[i] in occurrence and occurrence[pattern[i]] != s[i]:
                return False

            if s[i] not in values or pattern[i] == values[s[i]]:
                occurrence[pattern[i]] = s[i]
                values[s[i]] = pattern[i]
            else:
                return False

        return True
