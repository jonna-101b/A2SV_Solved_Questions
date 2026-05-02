from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        res = float('inf')

        def backtrack(i):
            nonlocal res

            if i == len(cookies):
                res = min(res, max(children))
                return

            seen = set()

            for j in range(k):
                if children[j] in seen:
                    continue
                seen.add(children[j])

                children[j] += cookies[i]
                backtrack(i + 1)
                children[j] -= cookies[i]

        backtrack(0)
        return res
