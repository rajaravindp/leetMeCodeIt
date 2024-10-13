def reverseArr(arr, start, end):
    if start >= end:
        return arr
    
    arr[start], arr[end] = arr[end], arr[start]
    return reverseArr(arr, start+1, end-1)

arr = [2, 3, 4, 1, 0]
print(reverseArr(arr, start=0, end=len(arr)-1))




def reverseArr2(arr, idx, n):
    if idx >= n//2:
        return arr
    arr[idx], arr[n-idx-1] = arr[n-idx-1], arr[idx]
    return reverseArr2(arr, idx+1, n)

arr = [2, 3, 4, 1, 0]
print(reverseArr2(arr, idx=0, n=5))

