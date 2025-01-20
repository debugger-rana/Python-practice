from array import *
arr=array('i',[])
n=int(input("enter the length of the array:"))
for i in range(n):
    x=int(input("enter the next value:"))
    arr.append(x)

#printing the original array
print(arr)
# printing the values of the array
for i in arr:
    print(i,end=" ")

# # enter a value to serach in the array
val=int(input("\nenter the value for search:"))
# k=0
# for e in arr:
#     if(e==val):
#         print(k)
#         break
#     k+=1
# else:
#     print("value not found")

# print(arr.index(val)) 
# #this will return the index of the value in the array