def sum_list(numbers):
    # Your code goes here
    res = 0
    for i in range(0, len(numbers)):
        res = numbers[i] + res
    return res
    pass

sum_list([10, -5, 7, 8, -2])