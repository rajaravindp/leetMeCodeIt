def printSubseq(s,t):
    if s == "" or len(s) == 0:
        print(t)
        return

    curr = s[0]
    x = s[1:]

    printSubseq(x, t + curr)
    printSubseq(x, t)

    return

s = "abc"
printSubseq(s, "")