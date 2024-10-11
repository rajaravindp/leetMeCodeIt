def checkSorted(arr):
    if (len(arr) == 0 or len(arr) == 1):
        return True
    
    if arr[0] > arr[1] :
        return False
    return checkSorted(arr[1:])

arr = [10, -2, 1, 3, 5, 10, 0]
print(checkSorted(arr))