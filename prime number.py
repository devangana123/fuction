def prime(num):
    i=1
    count=0
    while i<=num:
        if num%i==0:  
            count+=1
        i=i+1
    if count==2:
        print(num,"is the prime number")      
    else:
        print(num,"is the not prime number")   
prime(int(input("enter the number")))