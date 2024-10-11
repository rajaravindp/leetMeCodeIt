def remove_duplicates(s):
    res = ""
    for i in s: 
        if i not in res: 
            res = "{}{}".format(res, i)
    return res


    # Alternative Method:
    # res = ""
    # for i in s:
    #     if i not in res: 
    #         res += i
    # return res


remove_duplicates("programming")
