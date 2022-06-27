def dup(a):
    i=0
    b=[]
    while i<len(a):
        if a[i] in b:
            pass
        else:
            b.append(a[i])
        i=i+1
    print(b)
dup([1,2,3,3,3,3,4,5])