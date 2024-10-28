from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        arr = []

        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        arr = sorted(arr)
        
        head = ListNode(arr[0]) 
        current = head

        for value in arr[1:]:
            current.next = ListNode(value)
            current = current.next

        return head