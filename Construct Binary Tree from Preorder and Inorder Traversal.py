from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    # def display(self):
    #     print(self.val, end = " =>")
    #     if self.left:
    #         self.left.display()
    #     if self.right:
    #         self.right.display()



class Solution:
    def check_where(self, stack, look, order):
        appeared = False
        popped = None

        if order[look] < order[stack[-1].val]:
            appeared = True

        while not appeared:
            popped = stack.pop()

            if stack:
                if order[look] < order[stack[-1].val]:
                    appeared = True

            else:
                appeared = True
                
            
        return popped, stack



    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        stack = []
        root = None
        order = {inorder[i]: i for i in range(len(inorder))}

        for num in preorder:
            target = TreeNode(num)

            if stack:
                popped, stack = self.check_where(stack, num, order)

                if popped:
                    popped.right = target
                else:
                    stack[-1].left = target
                
            else:
                root = target
            
            stack.append(target)

        return root
