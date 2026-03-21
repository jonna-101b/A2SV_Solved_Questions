from typing import Optional, List

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], history: List[bool], index: int = 0) -> int:
            if root is None:
                return 0

            if index == len(history):
                history.append(root.val % 2 == 0)
            else:
                history[index] = root.val % 2 == 0
                
            curr = 0 if index == 0 or index == 1 or not history[index - 2] else root.val
            return curr + dfs(root.left, history, index + 1) + dfs(root.right, history, index + 1)

        return dfs(root, [])
