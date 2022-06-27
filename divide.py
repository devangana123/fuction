def div(a):
    if a%3==0 and a%5==0:
        print("Fizzbuzz")
    elif a%3==0:
        print("Fizz")
    elif a%5==0:
        print("buzz")
    else:
        print(a)
div(int(input("enter the number")))