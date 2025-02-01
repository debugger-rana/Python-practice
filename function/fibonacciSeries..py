def fibo(n):
    if(n<=0):
        print("unvalid range input ")
    else:
        a=0
        b=1
        if n==1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2,n):
                c=a+b
                if(c>n):break
                else:
                    print(c)
                    a=b
                    b=c

userInput= int(input("Enter a nuber to get its fibonacci series:"))

fibo(userInput)

#how can we acchive the state in which out last printed number should not be greter than the value of n we input 