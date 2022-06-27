# def perfect(num):
#     i=1
#     sum=0
#     while i<num:
#         if num%i==0:
#             sum=sum+i
#         i=i+1
#     if sum==num:
#         print(i,"is perfect number")
#     else:
#         print(i,"is not perfect number")  
# perfect(int(input("enter the number")))
        
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")