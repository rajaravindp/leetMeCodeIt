from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        _sum = 0
        if root.left and not root.left.left and not root.left.right:
            _sum += root.left.val
        _sum += self.sumOfLeftLeaves(root.left)
        _sum += self.sumOfLeftLeaves(root.right)

        return _sum