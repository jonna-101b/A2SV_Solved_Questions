from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trace = []

        while head:
            trace.append(head.val)
            head = head.next

        my_head = ListNode()
        dummy = my_head
        i = len(trace) - 1

        while i >= 0:
            node = ListNode(trace[i])
            my_head.next = node
            my_head = my_head.next
            i -= 1

        return dummy.next
