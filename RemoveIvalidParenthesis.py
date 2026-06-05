from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left_rem, right_rem = 0, 0
        for c in s:
            if c == '(':
                left_rem += 1
            elif c == ')':
                if left_rem == 0:
                    right_rem += 1
                else:
                    left_rem -= 1
        
        result = set()
        def dfs(index, path, left_count, right_count, left_rem, right_rem):
            
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    result.add(path)
                return
            
            char = s[index]
            if char == '(' and left_rem > 0:
                dfs(index + 1, path, left_count, right_count, left_rem - 1, right_rem)
            
            if char == ')' and right_rem > 0:
                dfs(index + 1, path, left_count, right_count, left_rem, right_rem - 1)
            if char not in '()':
                dfs(index + 1, path + char, left_count, right_count, left_rem, right_rem)
            
            elif char == '(':
                dfs(index + 1, path + char, left_count + 1, right_count, left_rem, right_rem)
            
            elif char == ')':
                if right_count < left_count:
                    dfs(index + 1, path + char, left_count, right_count + 1, left_rem, right_rem)
        
        dfs(0, "", 0, 0, left_rem, right_rem)
        
        return list(result)
