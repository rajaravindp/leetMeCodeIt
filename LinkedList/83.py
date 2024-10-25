from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        slow = head
        fast = slow.next
        while fast:
            if slow.val != fast.val:
                slow = fast
                fast = fast.next
            else:
                slow.next = fast.next
                fast = slow.next
        return head