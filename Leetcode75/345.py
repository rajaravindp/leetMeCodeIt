class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]
        lst = list()
        for i in range(len(s)):
            lst.append(s[i])
        start = 0
        end = len(s) - 1

        while start <= end:
            if lst[start] in arr and lst[end] in arr:
                lst[start], lst[end] = lst[end], lst[start]
                start += 1
                end -= 1
            elif lst[end] not in arr:
                end -= 1
            elif lst[start] not in arr:
                start += 1
        return "".join(lst)

st = "IceCreAm"
s = Solution()
print(s.reverseVowels(st))