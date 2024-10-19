from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # cnt = 0
        # for i in range(len(flowerbed)):
        #     if flowerbed[i] == 0:
        #         cnt += 1
        # if cnt % 2 != 0 and cnt == (n*2)+1:
        #     return True
        # return False

        start = 0
        while start < len(flowerbed) and n > 0:
            if flowerbed[start] == 1:
                start += 2
            elif start == len(flowerbed)-1 or flowerbed[start+1] == 0:
                flowerbed[start] = 1
                start += 2
                n -= 1
            else:
                start += 1
        if n == 0:
            return True
        return False


flowerbed = [1,0,0,0,0,1]
n = 2

s = Solution()
print(s.canPlaceFlowers(flowerbed, n))