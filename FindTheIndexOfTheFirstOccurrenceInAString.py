class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                j = 0
                found = True

                for curr in range(i, len(haystack)):
                    if j == len(needle):
                        break
                    elif haystack[curr] == needle[j]:
                        j += 1
                    else:
                        found = False
                        break

                if found and j == len(needle): return i

        return -1
