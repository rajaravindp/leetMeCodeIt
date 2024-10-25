from typing import List

class Solution:
    def reverseString(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)):
            arr.append(nums.pop())
        return arr

nums = ["h","e","l","l","o", " ", "w", "o", "r", "l", 'd', "!"]
s = Solution()
print(s.reverseString(nums))