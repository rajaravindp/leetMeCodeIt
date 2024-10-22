from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        _max = 0 
        diff = 0
        for i in range(len(gain)):
            diff = diff + gain[i]
            _max = max(_max, diff)
        return _max


# gain = [-5,1,5,0,-7]
gain = [-4,-3,-2,-1,4,3,2]

s = Solution()
print(s.largestAltitude(gain))