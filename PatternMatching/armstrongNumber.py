def isArmstrong(x):
    ln = len(str(x))
    res = []
    for i in str(x):
        res.append(int(i)**ln) 

    if sum(res) == x:
        return True
    else: 
        return False

isArmstrong(371)