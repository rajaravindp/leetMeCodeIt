from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def func(self, r):
        if not r:
            return None
        self.func(r.left)
        self.func(r.right)
        self.arr.append(r.val)
        return self.arr
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = list()
        if not root:
            return self.arr
        return self.func(root)