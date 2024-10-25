from typing import Optional
from collections import defaultdict

class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        map = defaultdict(int)
        curr = head
        value = None
        while curr:
            if curr not in map:
                map[curr] += 1
                curr = curr.next
            else:
                value = curr
                break
        return value
    
def create_cycle(values, pos):
    """Creates a linked list with the given values and introduces a cycle at 'pos'."""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_start = None

    for i, val in enumerate(values[1:], 1):
        current.next = ListNode(val)
        current = current.next
        if i == pos:  
            cycle_start = current

    current.next = cycle_start 
    return head

values = [3, 2, 0, -4]  
pos = 1  
head = create_cycle(values, pos)
s = Solution()
print(s.detectCycle(head=head))


