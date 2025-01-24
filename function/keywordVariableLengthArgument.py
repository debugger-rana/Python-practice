# def person(name,*data):
#     print(name)
#     print(data)

# person('John',30,'male',8777340292)

# #*args and **kwargs in Python
# *args and **kwargs are mostly used in function definitions.
#  *args and **kwargs allow you to pass a variable number of arguments to a function. 
# What variable means here is that you do not know before hand that how many arguments can be passed 
# to your function by the user so in this case you use these two keywords. 
# *args is used to send a non-keyworded variable length argument list to the function. 


def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('John',age=30,gender='male',phone_number=8777340292)