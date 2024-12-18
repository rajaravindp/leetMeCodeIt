from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def check(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        else:
            return root1.val == root2.val and self.check(root1.left, root2.right) and self.check(root1.right, root2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        else:
            return self.check(root.left, root.right)