def binsearch(arr, target): 
    start = 0
    end = len(arr) -1
    while start <= end: 
        mid = (end + start)//2
        if arr[mid] == target: 
            return arr[mid]
        elif target > arr[mid]: 
            start = mid + 1
        else: 
            end = mid - 1
    return -1

x = [2, 4, 5, 6, 8, 10]
res = binsearch(x, 8)
print(res)