# A decorator in Python is a design pattern that allows you to modify the behavior of a function or method. 
# Decorators are typically used to add functionality to existing code in a clean and readable way. 
# They are often used for logging, access control, instrumentation, caching, and more.


def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if(a<b):
            a,b=b,a
        return func(a,b)
    return inner

div1=smart_div(div)

div1(2,4)

