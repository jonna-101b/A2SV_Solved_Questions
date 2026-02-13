from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix2 = [[ matrix[j][i] for j in range(len(matrix) - 1, -1, -1)] for i in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = matrix2[i][j]
