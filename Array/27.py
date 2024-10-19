from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        start = 0
        while start < len(nums):
            if nums[start] == val:
                nums.remove(nums[start])
                start = 0
            else: 
                start += 1
        return nums

nums = [3,2,2,3]
val = 3
s = Solution()
print(s.removeElement(nums, val))