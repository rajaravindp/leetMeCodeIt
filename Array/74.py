from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        _len = len(matrix)
        
        x = 0
        while x < _len:
            if target in matrix[x]:
                return True
            else:
                x += 1
        return False