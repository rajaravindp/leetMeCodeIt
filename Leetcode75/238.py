# *
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l = [1]
        r = [1]

        for i in range(1, len(nums)):
            l.append(l[-1] * nums[i-1])
            
        for j in range(len(nums)-2, -1, -1):
            r.append(r[-1] * nums[j+1])

        r = r[::-1]
        ans = []

        for i in range(len(l)):
            ans.append(l[i]*r[i])

        return ans
            
nums = [1,2,3,4]
# Output: [24,12,8,6]
# nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
s = Solution()
print(s.productExceptSelf(nums))