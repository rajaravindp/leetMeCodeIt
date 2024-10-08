def merge_two_sorted_lists(list1, list2):
    """
    Merged array must also be sorted
    """
    res = list()
    for i in list1: 
        res.append(i)
    for i in list2: 
        res.append(i)
    
    for i in range(len(res) - 1):
        swp = False
        for j in range(len(res) - i - 1):
            if res[j] > res[j+1]:
                res[j], res[j+1] = res[j+1], res[j]
                swp = True
        if not swp:
            return res
    pass

list1 = [1, 4, 7]
list2 = [2, 3, 5, 8]
merge_two_sorted_lists(list1, list2)