from array import *
#array is a collection of similar type of elements


# val=array('i',[1,2,3,4,5,6,7,8,9,10])
# print(val)
# #this will return 2 pparameter . 1st is the address of the array and 2nd is the size of the array
# print(val.buffer_info())
# #will print the type of code we are working with
# print(val.typecode)

# print(val.reverse())
# for i in range(len(val)):
#     print(val[i])


# print(id(val))

# help(array)

# for i in range(len(val)):
#     print(val[i])

# # what if you want to work with character array
# val=array('u',['a','e','i','o','u'])

# #waht to create a new array from the existing array

# newArr=array(val.typecode,(a for a in val))
# for e in newArr:
#     print(e)

# retry
# arr1= array('i',[1,2,3,4,5,6,7,8,9,10])

# newArr1=array(arr1.typecode, ( a*a for a in arr1))
# for i in newArr1:
#     print(i)

#printing using while loop
arr1= array('i',[1,2,3,4,5,6,7,8,9,10])
i=0
while i<len(arr1):
    print(arr1[i],end=" ")
    i+=1

