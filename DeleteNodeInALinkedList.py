# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next        
