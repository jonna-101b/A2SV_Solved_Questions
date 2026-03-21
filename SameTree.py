from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if None in (p, q) or p.val != q.val:
            return False 
                
        is_same = True
        if is_same:
            is_same = self.isSameTree(p.left, q.left)

        if is_same:
            is_same = self.isSameTree(p.right, q.right)

        return is_same
