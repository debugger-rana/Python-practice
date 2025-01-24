# # Types of Arguments in Python
# # Python provides various argument types to pass values to functions, making them more flexible and reusable. Understanding these types can simplify your code and improve readability. we have the following function argument types in Python:

# # Default argument
# # Keyword arguments (named arguments)
# # Positional arguments
# # Arbitrary arguments (variable-length arguments *args and **kwargs)
# # Lambda Function Arguments

# # Default Argument in Python Function 
# # Default arguments are the arguments that take a default value if no argument value is passed during the function call. 
# # You can provide a default value to an argument by using the assignment operator (=). 
# # If you do not provide a value to the argument, it will use the default value. 
# # The default argument must be at the end of the argument list. 
# # You can have multiple default arguments in a function.   


# # formal arguemt 
# def greet(name, msg = "Good morning!"):
#     print("Hello", name + ', ' + msg)

# # actual argument->positional argument , keyword argument , default argument , variable length argument
# # postion are important
# greet("rana","Kate")