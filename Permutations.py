class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        used=[False]*len(nums)
        def prem(cur):
            if len(cur)==n:
                ans.append(cur[:])
                return

            for j in range(n):
                if used[j]:
                    continue
                used[j]=True
                cur.append(nums[j])
                prem(cur)
                cur.pop()
                used[j]=False


        prem([])
        return ans 
