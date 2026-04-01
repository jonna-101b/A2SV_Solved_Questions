class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums=[k for k in range(1,n+1)]
        curr=0

        while len(nums)>1:
            curr=(curr+k-1)%len(nums)
            nums.pop(curr)

        return nums[0]
