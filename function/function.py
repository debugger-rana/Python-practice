# def function2(msg, times):
#     print(msg*times)

# function2("Hello\n", 3)
# function2(2,4)
# # function2('hello','world\n')  # TypeError: can't multiply sequence by non-int of type 'str'

# def function(time):
#     message='hello world\n'
#     return message*time

# print(function(3))

# # you can return multiple values from a function
# def function3():
#     return 1,2,3

# print(function3())



# # you can return and accept two values 
# def add_sub(a,b):
#     return a+b , a-b

# add, sub=add_sub(5,5)
# print(add)
# print(sub)

# Python’s argument-passing model is neither “Pass by Value” nor “Pass by Reference” 
# but it is “Pass by Object Reference”. 
# Depending on the type of object you pass in the function, the function behaves differently. 
# Immutable objects show “pass by value” whereas mutable objects show “pass by reference”.
# and the object reference is passed to the function.