class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res=""
        count=0
        total=3*(2**(n-1))

        def dfs(curset):
            nonlocal count
            nonlocal res
            
            if len(curset)==n:
                count+=1
                if count==k:
                    res+="".join(curset)
                return 
            
            for ch in "abc":
                if not curset or curset[-1]!=ch:
                    curset.append(ch)
                    dfs(curset)
                    curset.pop()
        if total<k: return ""
        dfs([])
        return res
