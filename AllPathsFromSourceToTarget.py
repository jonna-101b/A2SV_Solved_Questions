from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        paths = []

        def DFS(node, path) -> None:
            path.append(node)

            if node == n:
                paths.append(path.copy())
            else:
                for i in graph[node]:
                    DFS(i, path)

            path.pop()

        DFS(0, [])
        return paths
