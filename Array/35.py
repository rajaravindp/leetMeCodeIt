from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        else:
            start = 0
            while start <= len(nums)-1:
                if target > nums[start]:
                    start += 1
                else:
                    return start

# nums = [1, 3]
# target = 2
nums = [1,3,5,6]
# target = 2
target = 7
s = Solution()
print(s.searchInsert(nums, target))