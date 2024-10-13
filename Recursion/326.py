class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n == 0:
            return False
        if n == 1:
            return True
        
        res = self.isPowerOfThree(n//2)
        if res % 3 == 0:
            return True
        return False