def lastIndexEle(arr, n):
    if len(arr) == 0:
        return -1
    
    elif len(arr) == 1:
        return 0
    
    elif n not in arr:
        return -1
    
    if arr[-1] == n:
        return len(arr) - 1
    return lastIndexEle(arr[:-1], n)


arr = [2, 3, 5, 6, 8, 10, 11]
print(lastIndexEle(arr, 6))
