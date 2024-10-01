class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        d = ListNode(0)
        d.next = head
        curr = head
        prev = d

        while curr:
            after = curr.next
            if curr.val == val:
                prev.next = after
            else: 
                prev = curr
            curr = after

        return d.next