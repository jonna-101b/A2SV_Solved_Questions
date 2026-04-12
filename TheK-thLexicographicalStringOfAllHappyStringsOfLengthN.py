from typing import List

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ["a", "b", "c"]
        res = ""
        count = 0

        def find(index: int = 0, path: List = []):
            nonlocal res
            nonlocal count

            if len(path) == n:
                count += 1
                if not res and count == k:
                    res = "".join(path)
                
                return 

            for i in range(len(letters)):
                if path and i == index:
                    continue

                path.append(letters[i])
                find(i, path)
                path.pop()

                if res:
                    return
            
            return
        
        find()
        return res
