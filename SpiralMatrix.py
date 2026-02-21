class Solution:
    def checkCondition(self, pos: int, limit: int, increasing: bool) -> bool:
        if increasing:
            return pos < limit
        
        return pos > limit
    
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        spiral = []
        dxn = [1, 1]  # horzontal dxn, vertical dxn
        pos = [0, 0] # horizontal position, vertical position
        curr_dxn = 0
        limits = [[len(matrix[0]), -1], [len(matrix), 0]] # horizontal limits, vertical limits
        counter = 0
        size = len(matrix) * len(matrix[0])

        while counter < size:
            curr_limit = 0 if dxn[curr_dxn] == 1 else 1

            while self.checkCondition(pos[curr_dxn], limits[curr_dxn][curr_limit], dxn[curr_dxn] == 1):
                spiral.append(matrix[pos[1]][pos[0]])
                pos[curr_dxn] += dxn[curr_dxn]
                counter += 1

            pos[1 - curr_dxn] += dxn[1 - curr_dxn]
            dxn[curr_dxn] *= -1
            pos[curr_dxn] += dxn[curr_dxn]
            limits[curr_dxn][curr_limit] += dxn[curr_dxn]
            curr_dxn = 1 - curr_dxn

        return spiral
