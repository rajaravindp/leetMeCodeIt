class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        map = {}
        while curr:
            num = curr.val
            if num in map: 
                map[num] += 1
            else: 
                map[num] = 1
            curr = curr.next
        
        d = ListNode()
        current = d
        for key, val in map.items():
            current.next = ListNode(val)
            current = current.next
        return d.next


