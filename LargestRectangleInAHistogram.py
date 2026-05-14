from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []  
        area = 0
        n = len(heights)
        
        for i in range(n):
            
            while stk and heights[stk[-1]] > heights[i]:
                height = heights[stk.pop()]
          
                width = i if not stk else i - stk[-1] - 1
                area = max(area, height * width)
            
            stk.append(i)
        
     
        while stk:
            height = heights[stk.pop()]
            width = n if not stk else n - stk[-1] - 1
            area = max(area, height * width)
        
        return area
