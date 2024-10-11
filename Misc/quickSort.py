def partition(arr, lb, ub):
    start = lb
    end = ub
    p = arr[lb]
    while start < end: 
        while start < ub and arr[start] <= p:
            start += 1
        while end > lb and arr[end] > p:
            end -= 1
        if start < end: 
            arr[start], arr[end] = arr[end], arr[start]
    arr[lb], arr[end] = arr[end], arr[lb]
    return end


def quickSort(arr, lb, ub):
    if lb < ub:
        loc = partition(arr, lb, ub)
        quickSort(arr, lb, loc -1)
        quickSort(arr, loc +1, ub)
        return arr
    

arr = [9, 2, 3, 1, 0, -1, -7, 8, 4]
print(quickSort(arr, 0, len(arr)-1))


