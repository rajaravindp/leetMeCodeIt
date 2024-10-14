def fact(x):
    if x == 0:
        return 1
    return fact(x-1) * x
def combinationFormula(n, r):
    f1 = fact(n)
    f2 = fact(r)
    f3 = fact(n-r)
    return f1/(f2*f3)
print(combinationFormula(10, 3))