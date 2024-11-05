from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def height(self, r):
        if not r:
            return 0
        elif r.left and r.right:
            return 1 + min(self.height(r.left), self.height(r.right))
        elif not r.left:
            return 1 + self.height(r.right)
        elif not r.right:
            return 1 + self.height(r.left)
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        a = self.height(root.left)
        b = self.height(root.right)
        if not a:
            return 1 + b
        elif not b:
            return 1 + a
        elif a == b:
            return a + 1
        else:
            return min(a, b) + 1