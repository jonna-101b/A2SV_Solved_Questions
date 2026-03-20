from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
      
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = []
        dummy_one = reverse
        dummy_two = head
        maximum = []

        while head:
            reverse.append(head.val)
            head = head.next

        for i in range(len(reverse) - 1, -1, -1):
            if maximum:
                maximum.append(max(maximum[-1], reverse[i]))
            else:
                maximum.append(reverse[i])


        head = ListNode()
        dummy_three = head
        for i in range(len(maximum) - 1, -1, -1):
            if dummy_two.val == maximum[i]:
                head.next = ListNode(maximum[i])
                head = head.next
            
            dummy_two = dummy_two.next

        return dummy_three.next
