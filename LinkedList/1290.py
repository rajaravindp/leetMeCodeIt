class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        d = [curr.val]
        while curr and curr.next: 
            curr = curr.next
            d.append(curr.val)
        dec = 0
        for bit in d: 
            dec = dec * 2 + bit
        return dec