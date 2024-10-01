class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Create copy of the original list
        original = head
        head1 = ListNode(head.val)
        original = original.next
        copy = head1
        while original: 
            copy.next = ListNode(original.val)
            copy = copy.next
            original = original.next        
        # Reverse the list
        before = None
        curr = head
        while curr:
            after = curr.next
            curr.next = before
            before = curr
            curr = after
        # Compare original and reversed lists
        copy = head1
        while before:
            if before.val != copy.val:
                return False
            before = before.next
            copy = copy.next
        return True