def check_unique(lst):
    res = list()
    for i in lst:
        if i not in res: 
            res.append(i)
    if res == lst:
        return True
    else: 
        return False
            
    pass

check_unique([1, 2, 3, 3, 4, 5])