class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        map = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

        left = 0
        if len(num) == 0:
            return True
        if len(num) == 1:
            if num[0] == "0" or num[0] == "1" or num[0] == "8":
                return True
            else:
                return False
        res = []
        while left <= len(num)-1:
            if num[left] not in map:
                return False
            res.append(map[num[left]])

            left += 1
        
        ans =  "".join(res)
        return ans[::-1] == num


s = Solution()
print(s.isStrobogrammatic("106901"))
print(s.isStrobogrammatic("106601"))