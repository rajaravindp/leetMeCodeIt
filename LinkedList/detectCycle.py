from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # slow_val = slow.val
            # fast_val = fast.val
            if slow == fast:
                break
        else:
            return None
        slow = head
        while slow != fast:
            slow_val = slow.val
            fast_val = fast.val
            slow = slow.next
            fast = fast.next
        return slow


def createLinkedListWithCycle(arr: list[int], pos: int) -> Optional[ListNode]:
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
print(s.detectCycle(head))