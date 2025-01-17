a=int(input("Enter a number: "))
for i in range(2,a+1):
    if a%i==0:
        print(" NotPrime number")
        break
    else:
        print("Is a prime number")
        break
