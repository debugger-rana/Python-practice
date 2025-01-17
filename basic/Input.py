try:
    x = int(input('Enter first number: '))

    y = int(input('Enter second number: '))
    print('Sum of two numbers:',x + y)
except ValueError:
    print("Invalid input. Please enter valid integers.")