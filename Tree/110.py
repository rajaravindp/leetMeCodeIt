from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def func(self, r):
        if not r:
            return 0
        a = self.func(r.left)
        b = self.func(r.right)
        if abs(a-b) > 1:
            self.bool = False
        return 1 + max(a, b)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bool = True
        self.func(root)
        return self.bool    