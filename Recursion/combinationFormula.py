def combinationFormula(n, r):
    if r == 0 or n == r:
        return 1
    
    return combinationFormula(n-1, r-1) + combinationFormula(n-1, r)
print(combinationFormula(10, 3))