res = []
def binSearch(arr, n, start = 0, end = None):
    if len(arr) == 0:
        return None
    if n not in arr: 
        return None

    end = len(arr)-1
    mid = (start + end)//2

    if n < mid:
        return binSearch(arr, n, start, )

arr = [4, 1, 1, 2, 3, 5, 1]
n = 1
print(binSearch(arr, n))
    