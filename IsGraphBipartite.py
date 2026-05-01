class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(node, c):
            if node in color:
                return color[node] == c
            
            color[node] = c
            
            for neighbor in graph[node]:
                if not dfs(neighbor, 1 - c):
                    return False
            
            return True

        for i in range(len(graph)):
            if i not in color:
                if not dfs(i, 0):
                    return False
        
        return True
