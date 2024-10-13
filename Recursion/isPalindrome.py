def isPalindrome(s, start, end):
    if start >= end:
        return True
    res = isPalindrome(s, start+1, end-1)
    if s[start] != s[end]:
        return False
    else: 
        return res
s = "dexed"
print(isPalindrome(s, start=0, end=len(s)-1))


def isPalindrome2(s, idx):
    n = len(s)
    if idx > n//2:
        return True
    
    if s[idx] != s[n-idx-1]:
        return False
    return isPalindrome2(s, idx+1)

s = "madam"
print(isPalindrome2(s, idx=0))

