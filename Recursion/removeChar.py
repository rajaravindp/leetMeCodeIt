def removeChar(s, c):
    if not s or s == '':
        return s
    
    res = removeChar(s[1:], c)
    if s[0] == c:
        return res
    else: 
       return s[0] + res   

print(removeChar("good morrow", 'o'))