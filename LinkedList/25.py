from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # leng = 1
        # tail = head
        # while tail and tail.next:
        #     tail = tail.next
        #     leng += 1
        
        # slow = head
        # fast = head.next
        # if k * 2 > leng:
        #     for _ in range(k-1):
        #         slow = slow.next

        #     second = slow.next
        #     slow.next = None

        #     # Only reverse 1 st half
        #     prev = None
        #     while head:
        #         temp = head.next
        #         head.next = prev
        #         prev = head
        #         head = temp
            
        #     d = ListNode(0)
        #     d.next = prev
        #     while prev and prev.next:
        #         prev = prev.next
        #     prev.next = second
        #     return d.next

        # else:
        #     for _ in range(k-1):
        #         slow = slow.next
        #         fast = fast.next.next
            
        #     second = slow.next
        #     rest = fast.next
        #     slow.next = None
        #     fast.next = None

        #     # reverse 1st and second halves
        #     prev = None
        #     while head:
        #         temp = head.next
        #         head.next = prev
        #         prev = head
        #         head = temp

        #     prev1 = None
        #     while second:
        #         temp = second.next
        #         second.next = prev1
        #         prev1 = second
        #         second = temp
            
        #     d = ListNode(0)
        #     d.next = prev
        #     # concat 
        #     while prev and prev.next:
        #         prev = prev.next
        #     prev.next = prev1

        #     while prev1 and prev1.next:
        #         prev1 = prev1.next
        #     prev1.next = rest

        #     return (d.next)            
            
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
        # reverse
        prev= None
        curr = head
        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head.next = self.reverseKGroup(curr, k)
        return prev

        
