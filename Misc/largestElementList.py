def find_largest(numbers):
    """
    Using Bubble Sort
    """
    # if not numbers:
    #     return None
    # elif len(numbers) == 1: 
    #     return numbers[-1]
    # for i in range(len(numbers) -1):
    #     for j in range(len(numbers)-i-1):
    #         swp = False
    #         if numbers[j] > numbers[j+1]:
    #             numbers[j],numbers[j+1]  = numbers[j+1], numbers[j]
    #             swp = True
    #     if not swp: 
    #         return numbers[-1]

    """
    Using Lin Search
    """
    largest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest

x = [-5, -10, -2, -1, -7]
find_largest(x)