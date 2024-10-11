def is_subsequence(s, t):
    a = 0
    b = 0

    while a < len(s) and b < len(t):
        if s[a] == t[b]:
            b += 1
        a += 1
    return b == len(t)

s = "abcde" 
t = "ace"
is_subsequence(s, t)