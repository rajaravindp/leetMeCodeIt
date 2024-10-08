def count_even_odd(arr):
    even = 0
    odd = 0
    for i in arr: 
        if i % 2 == 0:
            even += 1
        else: 
            odd += 1
    res = tuple()
    res = (even, odd)
    return res
    pass

lst = [1, 2, 3, 4, 5]
count_even_odd(lst)