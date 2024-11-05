from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def func(self, nums):
        if not nums:
            return None
        l, r = 0, len(nums)-1
        m = (l+r)//2
        node = TreeNode(nums[m])
        node.left = self.func(nums[l:m])
        node.right = self.func(nums[m+1:r+1])
        return node
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.func(nums)