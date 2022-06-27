def up_low(a):
    i=0
    count=0
    count1=0
    while i<len(a):
        if a[i]>="a" and a[i]<="z":
            count+=1
        elif a[i]>="A" and a[i]<="Z":
            count1+=1
        i=i+1
    print("the count of the lower letters",count)
    print("the count of the upper letters",count1)
up_low( 'The quick Brow Fox')
