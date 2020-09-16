# Function to add two numbers
def add(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        addition = int(num1 + num2)
        return addition
    except ValueError:
        raise ValueError('Works only with numbers')


# Function to subtract two numbers


def subtract(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        subtraction = int(num1 - num2)
        return subtraction
    except ValueError:
        raise ValueError('Works only with numbers')
# Function to multiply two numbers


def multiply(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        multiplication = int(num1*num2)
        return multiplication
    except ValueError:
        raise ValueError('Works only with numbers')
# Function to divide two numbers


def divide(num1, num2):
    if(num2 == 0):
        return 0
    try:
        num1 = int(num1)
        num2 = int(num2)
        division = num1/num2
        return division
    except ValueError:
        raise ValueError('Works only with numbers')
