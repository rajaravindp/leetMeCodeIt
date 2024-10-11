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
# print(selection_sort([5, 4, 3, 2, 1]))
print(selection_sort([]))