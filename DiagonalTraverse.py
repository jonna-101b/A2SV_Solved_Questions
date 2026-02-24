from typing import List

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        diagonals = []
        dxn = [[-1, 1], [1, -1]]
        pos = [0, 0]
        curr_dxn = 0
        limits = [len(matrix), len(matrix[0])]
        counter = 0
        size = len(matrix) * len(matrix[0])

        while counter < size:
            down, right = -1 < pos[0] < limits[0], -1 < pos[1] < limits[1]

            while down and right:
                diagonals.append(matrix[pos[0]][pos[1]])
                pos[0] += dxn[curr_dxn][0]
                pos[1] += dxn[curr_dxn][1]
                down, right = -1 < pos[0] < limits[0], -1 < pos[1] < limits[1]
                counter += 1

            curr_dxn = 1 - curr_dxn
            pos[0] += dxn[curr_dxn][0]
            pos[1] += dxn[curr_dxn][1]

            if right:
                pos[1] += 1
                
            elif down:
                pos[0] += 1
            else:
                if pos[1] + 1 == limits[1]:
                    pos[0] += 1 
                else:
                    pos[1] += 1 

        return diagonals
