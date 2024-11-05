from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt1 = 0
                cnt2 = 0
                j = i - 1

                while j >= 0 and nums[j] == 1:
                    cnt1 += 1
                    j += 1
                k = i + 1
                while k < len(nums) and nums[k] == 1:
                    cnt2 += 1
                    k += 1
                d[i] = [cnt1, cnt2]
        return d


nums = [0,1,1,1,0,1,1,0,1]
s = Solution()
print(s.longestSubarray(nums))
