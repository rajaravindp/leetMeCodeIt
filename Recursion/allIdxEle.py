# def allIdxEle(arr, n, idx = 0):
#     arrLen = len(arr)
#     if arrLen == 0:
#         return -1
#     elif n not in arr:
#         return -1
    
#     if idx == arrLen:
#         return []
    
#     res = allIdxEle(arr, n, idx +1)
    
#     if arr[idx] == n:
#         return [idx] + res
#     else:
#         return res



# print(allIdxEle([2, 3, 5, 4, 3, 5, 3], 15, 0))


def allIdxEle(arr, n, idx, lst):
    if len(arr) == 0:
        return []
    elif n not in arr:
        return []
    
    if idx == len(arr):
        return 
    
    res = allIdxEle(arr, n, idx + 1, lst)

    if arr[idx] == n:
        return lst.append(idx)
    else:
        res
    
    return lst[::-1]

lst = []
print(allIdxEle([2, 3, 5, 4, 3, 5, 3], 5, 0, lst))
