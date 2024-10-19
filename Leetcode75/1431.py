from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        start = 0
        arr = list()
        while start < len(candies):
            if candies[start] + extraCandies >= max(candies):
                arr.append(True)
            else:
                arr.append(False)
            start += 1
        return arr

# candies = [2,3,5,1,3]
# extraCandies = 3        
# candies = [4,2,1,1,2]
# extraCandies = 1 
candies = [12,1,12]
extraCandies = 10

s = Solution()
print(s.kidsWithCandies(candies, extraCandies))