class Solution: 
    def printNGE(self, arr):

        stk = []
        res = [-1] * len(arr)

        for i in range(len(arr)-1, -1, -1):
            curr = arr[i]
            while stk and stk[-1] <= curr:
                stk.pop()
            if stk:
                res[i] = stk[-1]
            stk.append(curr)

        return res

arr = [11, 13, 21, 3]
s = Solution()
print(s.printNGE(arr))