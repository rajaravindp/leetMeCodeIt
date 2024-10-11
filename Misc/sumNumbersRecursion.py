def sumNatNums(n):
    if n == 1:
        return 1
    if n == 0:
        return
    return n + sumNatNums(n-1)
    
print(sumNatNums(0))