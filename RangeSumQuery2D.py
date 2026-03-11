from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum = []

        for i in range(len(matrix)):
            self.prefix_sum.append([0])

            for j in range(len(matrix[i])):
                self.prefix_sum[i].append(self.prefix_sum[i][-1] + matrix[i][j])

        print(self.prefix_sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0

        for i in range(row1, row2 + 1):
            total += self.prefix_sum[i][col2 + 1] - self.prefix_sum[i][col1]

        return total
