from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    arr = list()
    for i in range(len(nums1)):
        arr.append(nums1[i])
    for j in range(len(nums2)):
        arr.append(nums2[j])

    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    if len(arr) % 2 != 0:
        res = (len(arr)-1)//2
        return arr[res]
    else:
        x = (len(arr)-1)//2
        y = x + 1
        return (arr[x] + arr[y])/2

nums1 =[1,2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))