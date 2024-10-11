def factorial(n):
    if n == 1:
        return 1
    
    res = n * factorial(n-1)
    
    return res

print(factorial(4))
# print(factorial(5))
# print(factorial(7))