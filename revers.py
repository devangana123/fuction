def rev(a):
    i=1
    b=[]
    while i<=len(a):
        b.append(a[-i])
        i=i+1
    print(b)
rev("1234abcd")