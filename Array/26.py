from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        x = 0
        while x < len(nums)-1:
            y = x + 1
            if nums[x] == nums[y]:
                nums.remove(nums[y])
                # x += 1
            else: 
                x += 1
        return len(nums)


nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
print(s.removeDuplicates(nums))