from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return (root.val == subRoot.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right))
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) or self.isSameTree(root, subRoot)