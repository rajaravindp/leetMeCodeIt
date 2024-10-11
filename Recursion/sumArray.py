def sum_array(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[-1]
    
    res = arr[0] + sum_array(arr[1:])

    return res
# print(sum_array([1, 2, 3, 4, 5, 6]))
print(sum_array([]))