class Solution:
    def isSubsequence(self, s: str, t: str):

        # def splitter(x):
        #     arr = list()
        #     for i in range(len(x)):
        #         arr.append(x[i])
        #     return arr

        # a = splitter(s)
        # b = splitter(t)

        # i = 0
        # j = 0
        # map = {}
        # for _ in range(len(a)):
        #     while j < len(b):
        #         if a[i] != b[j]:
        #             j += 1
        #         else:
        #             map[j] = b[j]
        #             j+=1
        #             break
        #     i += 1
        #     j = i
        # return [map[key] for key in sorted(map.keys())] == a

        i = 0
        j = 0
        while i <len(s) and j<len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


s = "acb"
t = "ahbgdc"

sol = Solution()
print(sol.isSubsequence(s, t))