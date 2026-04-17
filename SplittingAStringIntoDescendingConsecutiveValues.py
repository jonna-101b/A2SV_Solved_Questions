from typing import List

class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        
        def dfs(index, prev):
            if index == n:
                return True
            
            num = 0
            for j in range(index, n):
                num = num * 10 + int(s[j])
                
                if num == prev - 1:
                    if dfs(j + 1, num):
                        return True
                elif num >= prev:
                    break
            
            return False
        for i in range(1, n):
            first = int(s[:i])
            if dfs(i, first):
                return True
        
        return False
