from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrows = 1
        points.sort(key=lambda x: x[1])
        current_arr = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > current_arr:
                arrows += 1
                current_arr = points[i][1]
        return arrows
        # [[1,6], [2,8], [7,12], [10,16]]
