from typing import List

class Bomb:
    def __init__(self, id: int) -> None:
        self.id = id
        self.detonates = []

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        bombRecord = {i: Bomb(i) for i in range(n)}

        # Build graph
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(i+1, n):
                x2, y2, r2 = bombs[j]
                dx = x1 - x2
                dy = y1 - y2
                dist_sq = dx * dx + dy * dy

                if dist_sq <= r1 * r1:
                    bombRecord[i].detonates.append(j)
                if dist_sq <= r2 * r2:
                    bombRecord[j].detonates.append(i)

        # DFS to count reachable bombs
        def dfs(start):
            visited = set()

            def visit(node):
                if node in visited:
                    return
                visited.add(node)
                for nei in bombRecord[node].detonates:
                    visit(nei)

            visit(start)
            return len(visited)

        # Try starting from each bomb
        maximum = 0
        for i in range(n):
            maximum = max(maximum, dfs(i))

        return maximum
