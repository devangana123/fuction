# def str1(a):
#     i=0
#     count=0
#     while i<len(a):
        
#         count+=1
#         i=i+1
#     print(count) 
# str1(['abc', 'xyz', 'aba', '1221'])      

def pal(name):
    length=len(name)
    i=0 
    a=[]
    while i<length:
        length-=1
        print(name[length])
        a.append(name[length])
        i=i+1
    if a==name:
        pass
    print(length)
pal(['abc', 'xyz', 'aba', '1221'])   