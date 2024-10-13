def merge(arr, start, end, mid):
    a = start
    b = mid + 1
    res = []

    while (a<=mid and b<=end):
        if (arr[a] < arr[b]):
            res.append(arr[a])
            a += 1
        elif (arr[a] > arr[b]):
            res.append(arr[b])
            b += 1
        else:
            res.append(arr[a])
            res.append(arr[b])
            a += 1
            b += 1
    while (a <= mid):
        res.append(arr[a])
        a += 1
    while (b <= end):
        res.append(arr[b])
        b += 1
    
    for i in range(len(res)):
        arr[start + i] = res[i]

def mergeSortHelper(arr, start, end):
    if start >= end:
        return

    mid = start + (end - start)//2

    mergeSortHelper(arr, start, mid)
    mergeSortHelper(arr, mid + 1, end)
    merge(arr, start, end, mid)

    return

def mergeSort(arr):
    mergeSortHelper(arr, start=0, end=len(arr)-1)
    return arr

arr = [3, 1, 0, 8, 4, -1]
print(mergeSort(arr))