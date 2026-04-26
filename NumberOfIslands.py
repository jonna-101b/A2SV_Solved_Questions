from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [ [False]*m for _ in range(n) ]
        count = 0

        def DFS(r, c):
            nonlocal n, m
            if r < 0 or r >= n:
                return
            
            if c < 0 or c >= m:
                return

            if visited[r][c] or grid[r][c] == "0":
                return

            visited[r][c] = True
            DFS(r+1, c)
            DFS(r-1, c)
            DFS(r, c+1)
            DFS(r, c-1)
            return

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "1":
                    DFS(i, j)
                    count += 1

        return count
