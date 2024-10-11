def sum_of_even_numbers(n):
    arr = []
    for i in range(1, n*2+1):
        if i % 2 == 0:
            arr.append(i)
    return sum(arr)
    
    pass

sum_of_even_numbers(3)
