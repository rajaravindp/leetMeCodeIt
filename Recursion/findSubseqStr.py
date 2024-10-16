def findSubseq(s):
    res = list()
    if not s or len(s) == 0:
        res = ['']
        return res
    
    sa = findSubseq(s[1:])
    res.extend(sa)
    # print(res)
    # print(sa)

    for i in sa:
        res.append(s[0] + i)

    return res
    

s= "abc"
print(findSubseq(s))
        
    
    
    
