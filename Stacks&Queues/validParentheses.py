class Solution:
    def isValid(self, s: str) -> bool:
        map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for i in s:
            if i in map.keys():
                if stack and stack[-1] == map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        return False

s = "([{}])"        
sol = Solution()
print(sol.isValid(s))