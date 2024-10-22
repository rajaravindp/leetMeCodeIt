class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        # O(n * k)
        # start = 0
        # v = ['a', 'e', 'i', 'o', 'u']
        # cnt = 0
        # arr = []
        # while start < len(s)-k+1:
        #     for i in range(start, start+k): 
        #         if s[i] in v:
        #             cnt += 1
        #     arr.append(cnt)
        #     cnt = 0
        #     start += 1
        # return max(arr)        

        # O(n)
        v = set('aeiou')
        cnt = 0
        max_vcnt = 0

        for i in range(k):
            if s[i] in v:
                cnt += 1
        max_vcnt = cnt

        for i in range(k, len(s)):
            if s[i-k] in v:
                cnt -= 1
            if s[i] in v:
                cnt += 1
            max_vcnt = max(max_vcnt, cnt)
            
        return max_vcnt


s, k = "abciiidef", 3
# s = "aeiou"
# k = 2
# s = "loveyou"
# k = 7
sol = Solution()
print(sol.maxVowels(s, k))
