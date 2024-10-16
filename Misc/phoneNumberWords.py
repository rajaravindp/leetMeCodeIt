# Works for 2 numbers only

def phoneNumWords(input, idx = 0):
    if len(input) == 0:
        return
    
    inp = list()
    for i in input:
        inp.extend(i)
    
    k = [
        [], 
        [], 
        ["A", "B", "C"], 
        ["D", "E", "F"],
        ["G", "H", "I"],
        ["J", "K", "L"],
        ["M", "N", "O"],
        ["P", "Q", "R", "S"],
        ["T", "U", "V"],
        ["W", "X", "Y", "Z"]
    ]
    chars = list()
    for i in range(len(inp)):
        chars.append(k[int(inp[idx])])
        idx += 1
    
    res = list()
    res.extend(chars[0])
    res.extend(chars[1])
    for i in chars[0]:
        for j in chars[1]:
            res.append(i+j)
    return res

print(phoneNumWords('34'))