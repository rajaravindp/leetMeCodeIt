class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            k = (low + high)//2
            tt = 0
            for i in piles:
                tt += (i + k -1)//k
            if tt <= h:
                high = k-1
            else:
                low = k + 1
        return low        