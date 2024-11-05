from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = int("".join(map(str, nums)))
        curr_num = float('inf')
        start = 0
        while start < len(nums)-1:
            for i in range(len(nums)-1):
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    x = int("".join(map(str, nums))) 
                    if x > curr and x < curr_num:
                        curr_num = x
            start += 1
        return nums


nums = [1,2,3]
s = Solution()
print(s.nextPermutation(nums))