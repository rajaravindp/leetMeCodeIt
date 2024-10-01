class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        curr = head
        while curr: 
            for _ in range(m-1):
                if not curr.next: 
                    return head
                curr = curr.next
            
            temp = curr
            for _ in range(n):
                if not temp.next: 
                    break
                temp = temp.next

            curr.next = temp.next
            curr = curr.next
        return head