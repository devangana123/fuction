# def greet(*names):
#     for name in names:
#         print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")

def greet(*names):
    i=0
    while i<len(names):
        print("hellow",names[i])
        i=i+1
greet("sonu", "kartik","umesh", "bijender")


