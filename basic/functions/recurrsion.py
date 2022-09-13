def recursion(k):
    if(k>0):
        a=k+recursion(k-1)
        print(a)
    else:
        a = 0
    return a
recursion(10)