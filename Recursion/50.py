def myPow(x: float, n: int) -> float:

    # Does not work large values of n
    # if n == 0:
    #     return 1

    # if n > 0:
    #     if n == 1:
    #         return x

    #     res =  x* myPow(x, n-1)
    #     return res
    
    # if n < 0:
    #     if n == -1:
    #         return (1/x)
        
    #     res = 1/x * myPow(x, n + 1)
    #     return res

    if n == 0:
        return 1
    
    if n < 0:
        x = 1/x
        n = -n

    res = myPow(x, n // 2)

    if n % 2 == 0:
        return res * res
    else: 
        return res * res * x


    




# print(myPow(2.00000, 0))
# print(myPow(2.10000, 10))
# print(myPow(2.25, -10))
print(myPow(0.00001, 2147483647))
