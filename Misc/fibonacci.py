def fibonacci1(n):
    a = 0
    b = 1
    res = 0

    if n <= 1:
        return n
    for i in range(2, n+1):
        res = a + b
        a = b
        b = res
    return res

print(fibonacci1(8))
# print(fibonacci1(10))
# print(fibonacci1(7))