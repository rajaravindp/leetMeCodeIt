from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def convertToArray(ll):
            arr = list()
            curr = ll
            while curr:
                arr.append(curr.val)
                curr = curr.next
            return arr
        
        a = convertToArray(l1)
        a = int(''.join(map(str, a)))
        b = convertToArray(l2)
        b = int(''.join(map(str, b)))
        
        res = str(a + b)
        arr = list()
        for i in range(len(res)):
            arr.append(int(res[i]))

        d = ListNode(arr[0])
        curr = d
        
        for i in arr[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        return d