from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            # slow_val = slow.val
            # fast_val = fast.val
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

def createLinkedListWithCycle(arr, pos: int) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    nodes = [head]  
    for val in arr[1:]:
        new_node = ListNode(val)
        curr.next = new_node
        curr = new_node
        nodes.append(new_node)
    if pos != -1:
        curr.next = nodes[pos] 
    return head

arr = [3, 2, 0, -4]
pos = 1  
head = createLinkedListWithCycle(arr, pos)
s = Solution()
print(s.hasCycle(head))