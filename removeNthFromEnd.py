from ListNode import ListNode, createNode
from typing import *

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        left = dummy
        right = head
        # There are always n nodes b/w left and right
        while n > 0:
            right = right.next
            n -= 1
        # Once right goes off the end of list, left.next indicates the node to delete
        while right:
            left = left.next
            right = right.next
        # Delete left.next
        tmp = left.next
        left.next = tmp.next
        tmp.next = None
        return dummy.next
