from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        new_img = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]
        limits = (len(img), len(img[0]))

        for i in range(len(img)):
            for j in range(len(img[i])):
                directions = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
                total = 0
                n = 0

                for dxn in directions:
                    if -1 < dxn[0] < limits[0] and -1 < dxn[1] < limits[1]:
                        total += img[dxn[0]][dxn[1]]
                        n += 1

                new_img[i][j] = total // n

        return new_img
