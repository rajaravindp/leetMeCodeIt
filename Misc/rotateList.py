def rotate_list(lst, k):
    if not lst: 
        return []
    if k > len(lst):
         k = k % len(lst)
    res = []
    for i in range(-k, 0):
        res.append(lst[i])
    for i in res: 
        if i in lst: 
            lst.remove(i)
    for i in range(len(lst)): 
        res.append(lst[i])
    
    return res

    pass

lst = [10, 20, 30, 40, 50]
rotate_list(lst, 3)