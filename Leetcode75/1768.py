class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # start = 0
        # res = []
        # if len(word1) == len(word2):
        #     while start < len(word2):
        #         res.append(word1[start]+word2[start])
        #         start += 1
        # elif len(word1) < len(word2):
        #     while start < len(word1):
        #         res.append(word1[start]+word2[start])
        #         start += 1
        #     x = len(word1)
        #     for i in range(x, len(word2)):
        #         res.append(word2[i])
        # else:
        #     while start < len(word2):
        #         res.append(word1[start]+word2[start])
        #         start += 1
        #     x = len(word2)
        #     for i in range(x, len(word1)):
        #         res.append(word1[i])

        # print(res)
        # return "".join(res)


    # Using recursion
        if not word1:
            return word2
        if not word2:
            return word1
        
        return word1[0] + word2[0] + self.mergeAlternately(word1[1:], word2[1:])

word1 = "ab"
word2 = "pqrs"

s = Solution()
print(s.mergeAlternately(word1, word2))