# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        hash=defaultdict(int)
        hash[0]=1

        def dfs(root,runsum):
            if not root:
                return 0
            count=0
            runsum+=root.val
            count=hash[runsum-targetSum]
            hash[runsum]+=1

            count+=dfs(root.left,runsum)
            count+=dfs(root.right,runsum)
            hash[runsum]-=1
            return count
     
        return dfs(root,0)
