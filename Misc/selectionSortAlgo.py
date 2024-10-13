# https://visualgo.net/en/sorting

def selection_sort(lst):
    for i in range(0, len(lst)-1):
        temp = lst[i]
        minVal = lst[i]
        for j in range(i+1, len(lst)):
            if lst[j] < minVal:
                minVal = lst[j]
        minValIdx = lst.index(minVal)
        lst[i], lst[minValIdx] = minVal, temp
    return lst

# print(selection_sort([7, 5, 2, 8, 1]))
print(selection_sort([5, 4, 3, 2, 1]))
# print(selection_sort([]))


# Modified Selection Sort
def Selectionsort(arr, lb, start, end):

    while lb <= end:
        comp = start + 1
        min = arr[start]
        while comp <= end:
            if min <= arr[comp]:
                start += 1
                comp += 1
            else:
                min = arr[comp]
                start += 1
                comp += 1
        
        res = arr.index(min)
        arr[lb], arr[res] = arr[res], arr[lb]
        lb += 1
        start = lb 
    return arr


arr = [100, -1, 10, 9, -21, 6, 0, 1, 2, -15, -10, 1000, -1000, 999]
print(Selectionsort(arr, lb= 0, start=0, end=len(arr)-1))