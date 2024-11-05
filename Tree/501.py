from collections import Counter
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def func(self, r):
        if not r:
            return
        self.arr.append(r.val)
        self.func(r.left)
        self.func(r.right)
        return self.arr

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = list()
        if not root:
            return None
        arr = self.func(root)
        c = Counter(arr)
        max_value = max(c.values())
        return [key for key, value in c.items() if value == max_value]