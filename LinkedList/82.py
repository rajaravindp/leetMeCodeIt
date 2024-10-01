class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Build freq map
        prev = None
        curr = head
        map = {}
        while curr: 
            num = curr.val
            if num in map: 
                map[num] += 1
            else: 
                map[num] = 1
            curr = curr.next
        # print(map)

        # Append the keys to a list where val = 1
        lst = []
        for key, val in map.items():
            if (val == 1): 
                lst.append(key)
        # print(l)
        
        # Built a LL from the list
        if not lst: 
            return None

        d = ListNode(lst[0])
        c = d

        for i in lst[1:]:
            c.next = ListNode(i)
            c = c.next
        return d