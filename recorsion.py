def power(a,b):
    if b==0:
        return 1
    else:
        return (a*power(a,b-1))
x=int(input("enter the number :"))
y=int(input("enter its power :"))
z=power(x,y)
print(z)