class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        dx=set()
        dy=set()
        cols=set()
        ans=[["."]*n for _ in range(n)]
        res=[]

        def dfs(i):
            if i==n:
                res.append(["".join(k) for k in ans])
                return

            for j in range(n):
                if i-j not in dx and i+j not in dy and j not in cols:
                    ans[i][j]="Q"
                    dx.add(i-j)
                    dy.add(i+j)
                    cols.add(j)
                    dfs(i+1)
                    ans[i][j]="."
                    dx.remove(i-j)
                    dy.remove(i+j)
                    cols.remove(j)
        dfs(0)
        return res
