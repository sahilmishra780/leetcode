
from ListNode import ListNode, createNode
from typing import *

class Solution:
    def getKth(self, node, k):
        while k > 0 and node:
            node = node.next
            k -= 1
        return node
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prevGroupEnd = dummy
        while True:
            # get the kth element after prevGroupEnd
            kth = self.getKth(prevGroupEnd, k)
            if not kth:
                break
            
            nextGroupStart = kth.next
            prev, curr = kth.next, prevGroupEnd.next
            while curr != nextGroupStart:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = prevGroupEnd.next
            prevGroupEnd.next = prev
            prevGroupEnd = tmp
        return dummy.next 
    
Solution().reverseKGroup(createNode([1,2,3,4,5,6,7]), 3)