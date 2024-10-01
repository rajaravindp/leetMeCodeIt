class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before = None
        curr = head

        while curr: 
            after = curr.next
            curr.next = before
            before = curr
            curr = after
        return before