from numpy import *

arr=array([
    [1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]
])

print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)
# The itemsize attribute of a NumPy array returns the length of one array element in bytes. 
# This is determined by the data type (dtype) of the array elements.
print(arr.itemsize)

# fromm 2-d to 1-d array
print(arr.flatten())

# from 1-d to 2-d array-> rows and coloums 
print(arr.reshape(5,3))

