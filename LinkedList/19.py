# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        d = ListNode(0)
        d.next = head
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next
        
        if fast == None:
            return slow.next
        else:
            while fast.next:
                slow = slow.next
                fast = fast.next
        slow.next = slow.next.next

        return d.next     