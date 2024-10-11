def searchRange(nums, target):

    # Time complexity: O(n)
    # arr = []
    # if target not in nums:
    #     return [-1, -1]
    # i = 0
    # while i < len(nums):
    #     if nums[i] == target: 
    #         arr.append(i)
    #     i += 1
            
    # return arr

    # Time complexity: O(n**2)
    start = 0
    end = len(nums) -1
    arr = list()
    i = 0
    while i < len(nums)/2:
        if nums[start] == target:
            if start not in arr: 
                arr.append(start)
        if nums[end] == target:
            if end not in arr: 
                arr.append(end)
        start += 1
        end -= 1
        i += 1
    if not arr: 
        return [-1, -1]
    
    for i in range(len(arr)-1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return [arr[0], arr[-1]]            


    pass

nums = [5, 7, 7, 8, 8, 10]
target = 8
# nums = [5, 7, 7, 8, 8, 10]
# target = 6 
# nums = [1, 3, 4, 4, 4, 4, 5]
# target = 4
print(searchRange(nums, target))