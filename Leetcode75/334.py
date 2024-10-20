from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # O(n**3)
        # start = 0
        # for _ in range(0, len(nums)-2):
        #     a = start + 1
        #     while a < len(nums)-1:
        #         b  = a + 1
        #         while b < len(nums):
        #             if nums[start] < nums[a] and nums[a] < nums[b]:
        #                 return True
        #             else:
        #                 b += 1
        #         a += 1
        #     start += 1
        # return False

        # O(n)
        start = float('inf')
        end = float('inf')

        for i in nums:
            if i <= start:
                start = i
            elif i <= end:
                end = i
            else:
                return True
        return False


# nums = [1,2,3,4,5]        
nums = [5, 4, 3, 2, 1]        
# nums = [20,100,10,12,5,13]

s = Solution()
print(s.increasingTriplet(nums))