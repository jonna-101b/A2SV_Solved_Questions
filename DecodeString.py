from typing import List

class Solution:
    def oneTurn(self, s: str, i: int) -> List[str]:
        chars = []

        while i < len(s) and s[i] != "]":
            if s[i].isdigit():
                temp, i = self.decode(s, i)
                chars += temp

            elif s[i].isalpha():
                while i < len(s) and s[i].isalpha():
                    chars.append(s[i])
                    i += 1

            else:
                i += 1
                
        return chars, i + 1

    def decode(self, s: str, i: int) -> List[str]:
        if i >= len(s):
            return [], len(s)

        chars = []
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num *= 10
                num += int(s[i])
                i += 1

            for _ in range(num):
                if chars:
                    chars.append(chars[-1])

                else:
                    temp, i = self.oneTurn(s, i)
                    chars.append("".join(temp))

        else:
            temp = []
            while i < len(s) and s[i].isalpha():
                temp.append(s[i])
                i += 1

            chars.append("".join(temp))

        return chars, i

    def decodeString(self, s: str) -> str:
        chars = []
        i = 0

        while i < len(s):
            temp, i = self.decode(s, i)
            chars.append("".join(temp))

        return "".join(chars)
