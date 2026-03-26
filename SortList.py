# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next

        head = ListNode()
        dummy = head
        nums.sort()
        for num in nums:
            head.next = ListNode(num)
            head = head.next

        return dummy.next
