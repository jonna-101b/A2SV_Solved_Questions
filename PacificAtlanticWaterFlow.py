from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(starts, visited):
            q = deque(starts)

            for cell in starts:
                visited.add(cell)

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))

        # Pacific borders (top row + left column)
        pacific_starts = []
        for c in range(cols):
            pacific_starts.append((0, c))
        for r in range(rows):
            pacific_starts.append((r, 0))

        # Atlantic borders (bottom row + right column)
        atlantic_starts = []
        for c in range(cols):
            atlantic_starts.append((rows - 1, c))
        for r in range(rows):
            atlantic_starts.append((r, cols - 1))

        bfs(pacific_starts, pacific)
        bfs(atlantic_starts, atlantic)

        result = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
        
