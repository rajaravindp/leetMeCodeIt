from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        d = ListNode(0)
        for arr in lists:
            d.next = arr
            head = d.next
            while d and d.next:
                d = d.next
        
        arr = lists[0]

        lst = []
        while arr:
            lst.append(arr.val)
            arr = arr.next
        
        lst = sorted(lst)
        
        d = ListNode(0)
        curr = d
        for i in lst:
            curr.next = ListNode(i)
            curr = curr.next
        return d.next
