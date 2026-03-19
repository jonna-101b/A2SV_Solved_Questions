class Solution:
    def removeStars(self, s: str) -> str:
        reversed = []
        stars = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "*":
                stars += 1
                pass

            else:
                if stars:
                    stars -= 1

                else:
                    reversed.append(s[i])

        return "".join(reversed[::-1])
