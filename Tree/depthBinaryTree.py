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

        return 1 + max(self.func(r.left), self.func(r.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.func(root.left), self.func(root.right))