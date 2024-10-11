def is_palindromic_tuple(tup):
    if not tup or len(tup) == 1: 
        return True
    start = 0
    end = len(tup) - 1
    while start <= end: 
        if tup[start] != tup[end]:
            return False
        start += 1
        end -= 1
    return True
    pass

is_palindromic_tuple((1, 2, 3, 2, 1))