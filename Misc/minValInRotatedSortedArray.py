def findMin(nums):
    # Using Selection Sort
    for i in range(0, len(nums)-1):
        temp = nums[i]
        minVal = nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] < minVal:
                minVal = nums[j]
        minValIdx = nums.index(minVal)
        nums[i], nums[minValIdx] = minVal, temp
    return nums[0]
            
    pass


nums = [4, 7, 0, 1, 2] 
print(findMin(nums))