def max_consecutive_difference(lst):
    if not lst: 
        return None
    res = list()
    for i in range(len(lst)-1):
        x = abs(lst[i] - lst[i + 1])
        res.append(x)
    # return max(res)

    # Finding the max value using bubble sort
    for i in range(0, len(res) - 1):
        for j in range(len(res) - i - 1):
            if res[j] > res[j+1]:
                res[j], res[j+1] = res[j+1], res[j]
    return res
    pass

lst = [1, 7, 3, 10, 5]
max_consecutive_difference(lst)