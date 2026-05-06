from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        total = rows * cols
        
        # Directions: East, South, West, North
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        steps = 1  # number of steps to move in current direction
        r, c = rStart, cStart
        result.append([r, c])
        
        while len(result) < total:
            for i in range(4):
                dr, dc = directions[i]
                for _ in range(steps):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                        if len(result) == total:
                            return result
                if i % 2 == 1:
                    steps += 1
        
        return result
