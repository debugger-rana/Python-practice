nums=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(lambda n:n%2==0, nums))

print("even = ",evens)

double=list(map(lambda n:n*2, evens))

print("double = ",double)

from functools import reduce

sum=reduce(lambda a,b:a+b, double)

print("sum = ",sum)


