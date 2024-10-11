def firstIndexEle(arr, n):
    if len(arr) == 0:
        return -1
    
    elif len(arr) == 1:
        if arr[-1] == 2:
            return 1
        else:
            return -1
    
    elif n not in arr:
        return -1

    if arr[0] == n:
        return 0
    
    return firstIndexEle(arr[1:], n)+1

    

print(firstIndexEle([3, 2, 5, 2, 8, 2, 1], 8))