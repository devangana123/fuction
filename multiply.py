# def a(multy1,multy2):
#     i=0
#     while i<len(multy1):
#         c=multy1[i]*multy2[i]
#         print(c)
#         i=i+1
# a([2,3,5,6],[6,5,4,6])

# def a(multy):
#     i=0
#     p=-1
#     while i<len(multy):
#         b=multy[i]*multy[p]
#         p=p-1
#         if i==4:
#             break
#         i=i+1
#         print(b)
# a([1,2,4,6,7,2,7,8])     


def d(multy):
    i=0
    sum=1
    while i<len(multy):
        sum=sum*multy[i]
        i=i+1
        print(sum)
d([2,4,7,9,6,3,4])
