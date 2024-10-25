from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = [0]
        x = nums[0]
        for i in range(1, len(nums)):
            lsum.append(x)
            x += nums[i]
        
        rsum = [0]
        x = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            rsum.append(x)
            x += nums[i]
        
        rsum = rsum[::-1]

        # for i in range(len(lsum)):
        #     if lsum[i] == rsum[i]:
        #         return i
        # return -1 

        return lsum, rsum


nums = [1, 7, 3, 6, 5, 6]
s = Solution()
print(s.pivotIndex(nums))