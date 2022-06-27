def limit():
    multi=int(input("enter the number"))
    i=0
    sum=0
    while i<=multi:
        if i%3==0 or i%5==0:
            sum=sum+i
        i=i+1
    print(sum)
limit()