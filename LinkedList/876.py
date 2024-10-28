from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next

        cnt = 1
        curr = head
        while curr and curr.next:
            cnt += 1
            curr = curr.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if cnt % 2 != 0:
            return slow
        else:
            return slow.next