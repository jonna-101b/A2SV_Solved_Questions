# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_max(self, numbers: list[int]):
        m = max(numbers)
        for idx, n in enumerate(numbers):
            if n == m:
                return idx, m

    def split(self, numbers: list[int], at: int): 
        if at+1>len(numbers):
            return mumbers[0:at], []
        return numbers[0:at], numbers[at+1:]
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        
        idx, val = self.find_max(nums)
        left, right = self.split(nums, idx)
        tn = TreeNode(val)
        tn.left = self.constructMaximumBinaryTree(left)
        tn.right = self.constructMaximumBinaryTree(right)
        return tn
