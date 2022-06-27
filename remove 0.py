def n(num):
    if num%10!=0:
        print(num)
    else:
        n(num=num//10)
n(int(input("enter the number")))

