from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        start = 0
        end = 1
        res = list()
        while start < len(nums)-1:
            while end < len(nums):
                if nums[start] + nums[end] == target:
                    res.append(start)
                    res.append(end)
                    return res
                end += 1
            start += 1
            end = start + 1
        return res
    
arr = [1, 3,3]
target = 9
s = Solution()
print(s.twoSum(arr, target))