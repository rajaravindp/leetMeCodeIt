def is_palindrome(s):
    if not s:
        return True
    if len(s) == 1:
        return True
    res = []
    for i in s:
        if i != " ":
            i = i.lower()
            res.append(i)
    # start = 0
    # end = len(res) - 1
    # while start <= end: 
    #     if res[start] != res[end]:
    #         return False
    #     start += 1
    #     end -= 1
    # return True
    return res == res[::-1]

   
is_palindrome("A man a plan a canal Panama")