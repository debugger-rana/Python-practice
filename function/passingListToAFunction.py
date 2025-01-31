
# this show error but fix how to get list from user and use it in this code too
lst= input("Enter the number seperated by space :").split()
lst=int(lst)
print("list",lst)

def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd




even, odd =count(lst)

print(even)
print(odd)