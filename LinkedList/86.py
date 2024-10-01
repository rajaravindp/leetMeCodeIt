class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        
        prev = None
        curr = head
        l1 = []
        l2 = []
        while curr:
            if curr.val < x: 
                l1.append(curr.val)
            else: 
                l2.append(curr.val)
            curr = curr.next
        
        def create_ll(arr): 
            d = ListNode(arr[0])
            c = d

            if not arr: 
                return None
            for val in arr[1:]:
                c.next = ListNode(val)
                c = c.next
            return d
        
        h1 = create_ll(l1)
        h2 = create_ll(l2)

        if not h1:
            return None
        if not h2:
            return None
        
        cur = h1
        while cur.next: 
            cur = cur.next
        cur.next = h2

        return h1