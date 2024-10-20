from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Giving OOM exception
        # arr = []
        # start = 0
        # while start < len(height):
        #     for i in range(1, len(height)):
        #         y = min(height[start], height[i])
        #         x = i - start
        #         arr.append(x*y)
        #     start += 1
        # return max(arr) 

        maxArea = -1
        i = 0
        j = len(height)-1
        while(i<j):
            w = j-i
            h = min(height[i], height[j])
            maxArea = max(maxArea, h*w)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        
        return maxArea