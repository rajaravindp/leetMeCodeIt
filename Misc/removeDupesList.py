def remove_duplicates(lst):
    def sort_arr(lst): 
        for i in range(0, len(lst)- 1):
            swp = False
            for j in range(0, len(lst) - i - 1):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                    swp = True
            if not swp: 
                break
        return lst
    
    arr = sort_arr(lst)
    res = arr.copy()
    dup = 0
    for i in range(len(arr)):
        if arr[i] == dup:
            res.remove(arr[i])
            dup = arr[i]
        else: 
            dup = arr[i]
    return res



lst = [4, 5, 5, 4, 6, 7]
remove_duplicates(lst)