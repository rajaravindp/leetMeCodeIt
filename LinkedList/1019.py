from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        slow = head
        fast = head.next
        res = list()
        while slow.next:
            while fast:
                if slow.val > fast.val:
                    fast = fast.next
                elif slow.val < fast.val:
                    res.append(fast.val)
                    break
                else:
                    fast = fast.next
            else:
                res.append(0)
            slow = slow.next
            fast = slow.next
        res.append(0)
        return res