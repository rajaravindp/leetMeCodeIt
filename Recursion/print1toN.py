def count_to_n(n):
    if n <= 0:
        return
    
    count_to_n(n-1)

    print(n)

count_to_n(5)