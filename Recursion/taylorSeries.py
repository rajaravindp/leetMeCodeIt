p = 1
f = 1
def taylorSeries(x, n):
    global p, f
    if n == 0:
        return 1
    
    res =  taylorSeries(x, n-1)
    p *= x
    f *= n 
    return (res + p/f)

# print(taylorSeries(1, 4))
print(taylorSeries(4, 15))



# Alternative Method: Recursion
mul = 1
def taylorSeries1(x, n):
    global mul
    if n == 0:
        return mul
    mul = 1 + x/n * mul
    return taylorSeries1(x, n-1)
# print(taylorSeries1(1, 4))
print(taylorSeries1(1, 10))



# Using loop
# def taylorSeries2(x, n):
#     res = 1  
#     term = 1 
    
#     for i in range(1, n + 1):
#         term = term * (x / i)
#         res += term  
    
#     return res

# print(taylorSeries2(1, 4))



 