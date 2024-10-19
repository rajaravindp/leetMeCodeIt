from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) -1
        arr = list()
        mid = (end - start)//2
        
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        elif len(nums) % 2 != 0:
            while start < mid and end > mid:
                if nums[start] == target: 
                    arr.append(start)
                if nums[end] == target:
                    arr.append(end)
                if nums[mid] == target:
                    arr.append(mid)
                start += 1
                end -= 1
        elif len(nums) % 2 == 0:
            while start < end:
                if nums[start] == target: 
                    arr.append(start)
                if nums[end] == target:
                    arr.append(end)
                start += 1
                end -= 1
        if not arr: 
            return [-1, -1]
        arr = sorted(arr)
        return [arr[0], arr[-1]]


# nums = [1]
target = 1
nums = [5,7,7,8,8,10]
target = 8

s = Solution()
print(s.searchRange(nums, target))