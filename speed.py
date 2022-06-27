def speed(a):
    if a<=70:
        print("ok")
    else:
        diff=(a-70)//5
        if diff<=12:
            print(diff)
        else:
            print("lisence cancelled",diff)
x=int(input("enter the speed :"))
speed(x)

