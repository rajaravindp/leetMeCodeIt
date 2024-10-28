from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:

        numSet = set(nums)

        def helper(curr, comp):
            if not curr:
                return 0
            
            if curr.val in numSet:
                cnt = 0 if comp else 1
                return cnt + helper(curr.next, True)
            else:
                return helper(curr.next, False)
        return helper(head, False)