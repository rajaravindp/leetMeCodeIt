class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        odd = 0
        even = 0

        left = head
        right = head
        while right.next: 
            right = left.next
            if left.val > right.val: 
                even += 1
            else: 
                odd += 1
            left = right.next
        if odd > even: 
            return "Odd"
        elif even > odd: 
            return "Even"
        else: 
            return "Tie"
        