
# simple python calculator program


def add(num1, num2):   # add function
    result = num1 + num2
    print(num1, "+", num2, " = ", result)


def subtract(num1, num2):   # subtraction function
    result = num1 - num2
    print(num1, "-", num2, " = ", result)


def multiply(num1, num2):  # multiplication function
    result = num1 * num2
    print(num1, "*", num2, " = ", result)


def divide(num1, num2):   # division function
    result = num1 / num2
    print(num1, "/", num2, " = ", result)


# user input and choice of operation

select = int(input("Select 1, 2, 3 or 4 to choose an operation: "))

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if select == 1:
    add(num1, num2)
elif select == 2:
    subtract(num1, num2)
elif select == 3:
    multiply(num1, num2)
elif select == 4:
    divide(num1, num2)
else:
    print("You have entered an incorrect operation, Try again: ")
