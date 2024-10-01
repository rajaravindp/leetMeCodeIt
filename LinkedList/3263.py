class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        curr = root
        d = []
        while curr: 
            d.append(curr.val)
            curr = curr.next
        return d