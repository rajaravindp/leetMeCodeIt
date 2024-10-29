from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # 1
        # nums = sorted(nums)
        # return nums[0]

        # 2
        # _min = float("inf")
        # for i in nums:
        #     if i < _min:
        #         _min = i
        # return _min

        # 3
        left = 0 
        right = len(nums)-1

        while left < right:
            mid = (right + left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]