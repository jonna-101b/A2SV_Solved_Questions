class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        for n in range(len(nums)-2):
            if nums[n]==0:
                nums[n]=1
                nums[n+1]=0 if nums[n+1]==1 else 1
                nums[n+2]=0 if nums[n+2]==1 else 1
                count+=1

 
 

        return count if sum(nums)==len(nums) else -1
