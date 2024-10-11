def longest_word_length(s):
    # if len(s) == 0:
    #     return 0
    # res = list()
    # s = s.split()
    # for i in s: 
    #     if len(i) not in res: 
    #         res.append(len(i))
    
    # for i in range(0, len(res) - 1):
    #     for j in range(len(res) -i -1):
    #         if res[j] > res[j+1]:
    #             res[j], res[j+1] = res[j+1], res[j]
    
    # return res[-1]

    curr = 0
    maxm = 0

    for i in range(len(s)):
        if s[i] != " ":
            curr += 1
        else: 
            if curr > maxm:
                maxm = curr
            curr = 0
    if curr > maxm: 
        maxm = curr

    return maxm

s = "The quick brown fox"
print(longest_word_length(s))

 
