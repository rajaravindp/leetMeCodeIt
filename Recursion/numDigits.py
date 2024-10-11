def numDigits(n):
    if n >= 1 and n <=9:
        return 1
    
    sn = int(n/10)
    sa = 1 + numDigits(sn)

    return sa

print(numDigits(1012345))