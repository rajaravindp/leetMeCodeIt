from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        map = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] += 1
            else:
                map[nums[i]] = 1
        
        for i, j in map.items():
            if j > 1:
                return i


nums = [1,2,3,2,2]
s = Solution()
print(s.findDuplicate(nums))