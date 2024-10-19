class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        start = 0
        end = len(arr) - 1
        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr

s = "the sky is blue"
sol = Solution()
print(sol.reverseWords(s))
