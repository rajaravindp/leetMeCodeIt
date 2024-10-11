def x(n):
    if n == 0:
        return 0
    
    sa = x(n-1)
    res = n + sa

    return res

print(x(4))