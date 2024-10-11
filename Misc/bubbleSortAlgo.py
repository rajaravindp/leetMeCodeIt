# https://visualgo.net/en/sorting
def bubbleSort(arr):
    n = len(arr)
    for i in range(0, n-1):
        swp = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swp = True
        if not swp:
            break            
    return arr

bubbleSort([1, 2, 3, 4])
# bubbleSort([5, 2, 3, 1, 4, 0])