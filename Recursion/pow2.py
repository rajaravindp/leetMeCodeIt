def power_2(n):
    if n == 1:
        return 2

    sa = 2*power_2(n-1)
    # res = 
    return sa

print(power_2(5))