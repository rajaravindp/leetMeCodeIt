# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def app_lst(lst):
            arr = []
            while lst:
                arr.append(lst.val)
                lst = lst.next
            return arr
        
        x = app_lst(l1)
        y = app_lst(l2)

        carry = 0
        arr = []
        max_len = max(len(x), len(y))
        for i in range(max_len):
            if i < len(x):
                a = x[i]
            else:
                a = 0
            if i < len(y):
                b = y[i]
            else:
                b = 0
            
            _sum = a + b + carry
            carry = _sum // 10
            arr.append(_sum % 10)
        
        if carry:
            arr.append(carry)

        d = ListNode(0)
        curr = d
        for i in range(len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next
        return d.next