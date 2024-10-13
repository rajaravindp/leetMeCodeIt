def fact(n):
    if n == 1:
        return 1
    
    return n * fact(n-1)
    
print(fact(4))


def fact(n, idx = 3):
    if n < 1:
        return
    return idx