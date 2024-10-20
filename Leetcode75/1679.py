from itertools import count
from typing import Counter, List
from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        # O(n**2)
        start = 0
        cnt = 0
        for _ in range(start+1, len(nums)):
            end = len(nums)-1
            while start < end:
                if nums[start] > k:
                    start += 1
                elif nums[start] + nums[end] == k:
                    cnt += 1
                    nums.pop(end)
                    nums.pop(start)
                    end = len(nums)-1
                else:
                    end -= 1
            start += 1
        return cnt

        # O(n)
        # cnt = defaultdict(int)
        # ops = 0

        # for num in nums:
        #     diff = k - num
        #     if cnt[diff] > 0:
        #         ops += 1
        #         cnt[diff] -= 1
        #     else:
        #         cnt[num] += 1
        # return ops


        # Alt Solution
        # cnt = Counter(nums)
        # res = 0
        # print(cnt)
        # for i, j in cnt.items():
        #     if (k - i) in cnt:
        #         res += min(j, cnt[k-i])
        #         print(res)
        # return res//2

nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2
# nums = [3,1,3,4,3]
# k = 6
s = Solution()
print(s.maxOperations(nums, k))
