<<<<<<< HEAD
def fact(n):
    if n == 1:
        return 1
    
    return n * fact(n-1)
    
print(fact(4))


def fact(n, idx = 3):
    if n < 1:
        return
    return idx
=======
def x(n):
    if n == 0:
        return 0
    
    sa = x(n-1)
    res = n + sa

    return res

print(x(4))
>>>>>>> 3412204d1bc860432efe76bfbd07b6ff8eeb3e47
