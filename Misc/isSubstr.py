def is_substring(s, t):
    if not t:
        return True
    arr = s.split()
    arr1 = t.split()
    for i in arr1: 
        if i in arr:
            return True
    return False

s = "hello world"
t = "world"
is_substring(s, t)