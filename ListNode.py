import functools

@functools.lru_cache()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        current = self
        node_values = []
        while current:
            node_values.append(str(current.val))
            current = current.next
        return " -> ".join(node_values)

    def __repr__(self):
        return str(self)

def createNode(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        new_node = ListNode(val)
        current.next = new_node
        current = new_node

    return head
