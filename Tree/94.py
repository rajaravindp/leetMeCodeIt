from typing import Optional, List
from buildBinaryTree import TreeNode, BuildBinaryTree
from binaryTreeVisualizer import TreeVisualizer

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def myfunc(node, arr):
            if not node:
                return
            myfunc(node.left, arr)
            arr.append(node.val)
            myfunc(node.right, arr)

        arr = list()
        myfunc(root, arr=arr)
        return arr

data = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
root = BuildBinaryTree.build_tree(data)
# viz = TreeVisualizer(root)
# viz.plot_tree()
s = Solution()
print(s.inorderTraversal(root))
