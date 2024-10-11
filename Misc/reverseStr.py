def reverse_string(s):
    arr = []
    for i in s: 
        arr.append(i)
    
    start = 0
    end = len(arr) - 1
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return "".join(arr)



    # Alternative method:
    
    # reversed_str = ''
    # for i in range(len(s) - 1, -1, -1):
    #     reversed_str += s[i]
    # return reversed_str

reverse_string("hello")