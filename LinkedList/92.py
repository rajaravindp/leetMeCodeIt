# Wrong solution

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, lst):
            prev = None
            curr = lst
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        if left == right:
            return head
        if not head.next.next:
            return self.reverse(head)

        prev = ListNode(0)
        prev.next = head
        curr = head
        cnt = 1
        rev = None
        end = None
        while curr:
            if cnt == left:
                rev = prev.next
                prev.next = None
                temp = rev
                while temp:
                    if cnt == right:
                        end = temp.next
                        temp.next = None
                        break
                    else:
                        temp = temp.next
                        cnt += 1
                break
            else:
                curr = curr.next
                cnt += 1
                prev = prev.next

        mid = self.reverse(rev)
        
        temp = prev
        while temp and temp.next:
            temp = temp.next
        temp.next = mid
        
        temp = prev.next
        while temp and temp.next:
            temp = temp.next
        temp.next = end

        curr = prev
        while curr and curr.next:
            if curr.val == 0:
                curr = curr.next
                break
            break
        return curr