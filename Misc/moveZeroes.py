def move_zeroes(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(nums[i])
            nums.remove(nums[i])
    return nums
    pass

# nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
nums = [0, 0, 1]
print(move_zeroes(nums))
