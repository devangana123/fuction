def fact(n):
    if n==1:
        return 1                        #Base case, here is  we put the false condition
    else:
        return(fact(n-1))*n            #Recorsive case ,it's work like a loop,repeating
n=int(input("enter the number"))
a=fact(n)
print(a)