from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypads = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }
        res = []

        def combine(counter: int = 0, path: List[int] = []):
            if counter == len(digits):
                res.append("".join(path))
                return

            for char in keypads[digits[counter]]:
                path.append(char)
                combine(counter + 1, path)
                path.pop()

        combine()
        return res
