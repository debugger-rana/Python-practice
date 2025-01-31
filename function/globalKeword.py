# a=10 # golbal variable 
# b=30 
# def func():
#     a=20   #local variable
#     print(a,b)
# func()
# print(a,b)
# print(a)

# inside a function we can access global variable but we can not change the value of global variable ,
# if we want to change the value of global variable then we have to use global keyword

g=15
print("before function :",g)

def fun():
    global g  # this is effecting local variable and golbal variable too
    g=20
    print("from inside a function agter using global keyword :",g)

fun()

print("After the function :",g)


# if you want to change a golbal variable without effecting the local varialbe then in that case you will use (golbals())
a=10
print(a)
print(id(a))

def something():
    a=9
    x=globals()['a']
    print( id(x))
    print("in function", a)

globals()['a']=15
something()
print("outside function",a)
print(id(a))