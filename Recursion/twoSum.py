from typing import List

# Might face Recursion depth limit exceeded error for larger arr with more ele 
class Solution:
    def helper(self, nums, target, start=0, end=1):
        if start >= len(nums)-1:
            return None
        if nums[start] + nums[end] == target:
            return [start, end]
        if end == len(nums)-1:
            return self.helper(nums, target, start+1, start+2)

        return self.helper(nums, target, start, end = end+1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.helper(nums, target)
    
arr = [3, 2, 3]
target = 6
s = Solution()
print(s.twoSum(arr, target))