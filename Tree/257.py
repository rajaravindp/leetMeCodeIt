# Solution wrong

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
        return (self.func(r.left) or self.func(r.right))
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.arr = list()
        arr1 = list()
        if not root:
            return 
        if not root.left and not root.right:
            self.arr.append(str(root.val))
            return self.arr
        elif not root.left and root.right:
            self.arr.append(root.val) 
            self.func(root.right)
        elif root.left and not root.right:
            self.arr.append(root.val) 
            self.func(root.left)            
        else:
            self.arr.append(root.val) 
            self.func(root.left)
            self.arr.append(root.val) 
            self.func(root.right)
        b = self.arr.index(root.val, 1, len(self.arr))
        arr1 = self.arr[b:len(self.arr)]
        self.arr = self.arr[0:b]
        res = ""
        res = "->".join(str(num) for num in self.arr)
        res2 = ""
        res2 = "->".join(str(num) for num in arr1)
        arr2 = list()
        arr2.append(res)
        arr2.append(res2)
        return arr2