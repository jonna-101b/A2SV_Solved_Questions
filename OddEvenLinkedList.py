# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        even_head = ListNode()
        dummy_head = new_head
        dummy_even = even_head
        counter = 1

        while head:
            if counter % 2 == 0:
                even_head.next = head
                even_head = even_head.next
            else:
                new_head.next = head
                new_head = new_head.next

            head = head.next
            counter += 1

        even_head.next = None
        new_head.next = dummy_even.next

        return dummy_head.next
