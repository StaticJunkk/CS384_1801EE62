# Function to add two numbers
def add(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        addition = num1 + num2
        return addition
    except ValueError:
        raise ValueError('Works only with numbers')


# Function to subtract two numbers


def subtract(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        subtraction = num1 - num2
        return subtraction
    except ValueError:
        raise ValueError('Works only with numbers')
# Function to multiply two numbers


def multiply(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        multiplication = num1*num2
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


# Function to add power function
# You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2):  # num1 ^ num2
    # DivisionLogic
    return power

# Python 3 program to print GP.  geometric Progression
# You cant use the inbuilt python function. Write your own function


def printGP(a, r, n):
    gp = []
    return gp

# Python 3 program to print AP.  arithmetic Progression
# You cant use the inbuilt python function. Write your own function


def printAP(a, d, n):
    ap = []
    return ap

# Python 3 program to print HP.   Harmonic Progression
# You cant use the inbuilt python function. Write your own function


def printHP(a, d, n):
    hp = []
    return hp
