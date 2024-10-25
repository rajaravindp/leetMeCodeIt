# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        sec = slow.next
        slow.next = None
        prev = None
        while sec:
            temp = sec.next
            sec.next = prev
            prev = sec
            sec = temp

        sec = prev
        fir = head
        
        while sec:
            t1, t2 = fir.next, sec.next
            fir.next = sec
            sec.next = t1
            fir, sec = t1, t2

        
