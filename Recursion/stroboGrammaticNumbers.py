def stroboGrammaticNumber(s):
    odd_mid = ['0', "1", "8"]
    even_mid = ["00", "11", "69", "88", "96"]
    if s == 1:
        return odd_mid
    if s == 2:
        return even_mid 
    if s% 2 == 0:
        pre_num, mid_val = stroboGrammaticNumber(s-2), even_mid
    else:
        pre_num, mid_val = stroboGrammaticNumber(s-1), odd_mid

    mid = (s-1)//2
    res = []
    for i in mid_val:
        for j in pre_num:
            res.append(j[:mid] + i + j[mid:])
    return res

s = 3
print(stroboGrammaticNumber(s))
