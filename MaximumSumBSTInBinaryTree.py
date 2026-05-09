from typing import Optional

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0
        
        def dfs(node):
            if not node:
                return (True, 0, float('inf'), float('-inf'))
            
            left_is_bst, left_sum, left_min, left_max = dfs(node.left)
            right_is_bst, right_sum, right_min, right_max = dfs(node.right)
            
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                curr_sum = left_sum + right_sum + node.val
                
                self.max_sum = max(self.max_sum, curr_sum)
                
                return (
                    True,
                    curr_sum,
                    min(left_min, node.val),
                    max(right_max, node.val)
                )
            else:
                return (False, 0, 0, 0)
        
        dfs(root)
        return self.max_sum 
