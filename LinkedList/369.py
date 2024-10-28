class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        arr = list()

        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        num = int(''.join(map(str, arr)))
        num = str(num + 1)
        arr = []
        for i in range(len(num)):
            arr.append(int(num[i]))

        d = ListNode(arr[0])
        curr = d

        for i in arr[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        
        return d


