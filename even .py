# def oddeve(a):
#     if a%2==0:
#         print("even number")
#     else:
#         print("odd number")
# oddeve(int(input("enter the number")))
# oddeve(int(input("enter the number")))
# oddeve(int(input("enter the number")))


# def even(a):
#     i=0
#     b=[]
#     while i<len(a):
#         if a[i]%2==0:
#             b.append(a[i])
#         i=i+1
#     print(b)
# even([1, 2, 3, 4, 5, 6, 7, 8, 9])


a=[[1,2,3,4,5,],[6,7,8,9,1,2]]
i=0
while i<len(a):
    j=0
    b=[]
    while j<len(a[i]):
        c=a[i]+[j]
        b.append(c)
    i=i+1
print(b)
