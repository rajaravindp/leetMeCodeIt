from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        start = 0
        while start <= len(nums)-1:
            if nums[start] == 0:
                nums.append(nums[start])
                nums.remove(nums[start])
            start += 1
        # print(nums)
    
nums = [0,1,0,3,12]
s = Solution()

print(s.moveZeroes(nums))