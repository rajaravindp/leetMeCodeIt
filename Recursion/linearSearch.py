##### Head Recursion #####
# lst = []
# def linearSearch(arr, n, idx= 0):
#     if len(arr) == 0:
#         return None
#     elif idx == len(arr):
#         return None
#     elif n not in arr:
#         return None
    
#     res = linearSearch(arr, n, idx + 1)
#     if arr[idx] == n:
#         lst.insert(0, idx)
#     else:
#         return res

#     return lst

##### Tail Recursion #####
def linearSearch(arr, n, idx = 0, res = None):
    if res is None:
        res = []
    if len(arr) == 0:
        return None
    elif n not in arr:
        return None
    elif idx == len(arr):
        return res
    
    if arr[idx] == n:
        res.append(0, idx)

    return linearSearch(arr, n, idx + 1, res)

arr = [2, 0, 1, 3, 0, 5, 4, 0]
n = 0
print(linearSearch(arr, n))