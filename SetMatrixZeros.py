from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_zerod = set()
        col_zerod = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    row_zerod.add(row)
                    col_zerod.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row in row_zerod:
                    matrix[row][col] = 0

                if col in col_zerod:
                    matrix[row][col] = 0

        return matrix
