from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        

l1 = [2,4,3]
l2 = [5,6,4]
s = Solution()
s.addTwoNumbers(l1, l2)