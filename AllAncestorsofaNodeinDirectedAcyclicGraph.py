from collections import deque
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        ancestors = [set() for _ in range(n)]

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()

            for nei in graph[node]:

                ancestors[nei].add(node)

                ancestors[nei].update(ancestors[node])

                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return [sorted(list(s)) for s in ancestors]
