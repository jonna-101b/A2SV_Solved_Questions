class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count=defaultdict()
        left,ans=0,0

        for right in range(len(nums)):
            count[nums[right]]=count.get(nums[right],0)+1


            while len(count)>k:
                count[nums[left]]-=1
                if count[nums[left]]==0:
                    del count[nums[left]]
                left+=1        
            ans+=right-left+1
        
        count=defaultdict()
        left,coint=0,0

        for r in range(len(nums)):
            count[nums[r]]=count.get(nums[r],0)+1

            while len(count)>k-1:
                count[nums[left]]-=1
                if count[nums[left]]==0:
                    del count[nums[left]]
                left+=1
       
            coint+=r-left+1
        return ans-coint
        
