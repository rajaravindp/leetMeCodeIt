from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dep = 0
        if not root:
            return None
        def func(r):
            if not r:
                return 0
            left = func(r.left)
            right = func(r.right)
            self.max_dep = max(self.max_dep, left + right)
            return 1 + max(left, right)
        func(root)
        return self.max_dep