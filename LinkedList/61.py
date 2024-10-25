# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        fast = head
        k = k % length
        if k == 0:
            return head
        for _ in range(length - k - 1):
            fast = fast.next

        second = fast.next
        fast.next = None

        tail.next = head
        return second

        