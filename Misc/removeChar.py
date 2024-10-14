def removeChar(s, c):
    res = []
    for i in range(len(s)):
        res.append(s[i])
    
    for i in range(len(res)-1):
        if c in res:
            res.remove(c)
    
    return ''.join(res)
        

print(removeChar("good morning", 'o'))