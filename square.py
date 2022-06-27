def square(square1):
    j=1
    a=[]
    while j<=square1:
        m=j**2
        a.append(m)
        final=[]
        b=[]
        count=0
        i=0
        while i<len(a):
            if count==5:
                final.append(b)
                b=[]
                count=1
            else:
                count+=1
            b.append(a[i])
            i+=1
        final.append(b) 
        j=j+1
    print(final)
square(30)