# Function to add two numbers
def add(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        addition = num1 + num2
        return addition
    except ValueError:
        return 0


# Function to subtract two numbers


def subtract(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        subtraction = num1 - num2
        return subtraction
    except ValueError:
        return 0
# Function to multiply two numbers


def multiply(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        multiplication = num1*num2
        return multiplication
    except ValueError:
        return 0
# Function to divide two numbers


def divide(num1, num2):
    if(num2 == 0):
        return 0
    try:
        num1 = float(num1)
        num2 = float(num2)
        division = num1/num2
        return division
    except ValueError:
        return 0


# Function to add power function
# You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2):  # num1 ^ num2
    try:
        num1 = float(num1)
        num2 = int(num2)
        if(num2 == 0):
            return 1
        elif(num2 == 1):
            return num1
        else:
            x = num1
            if num2 > 0:
                for i in range(1, num2):
                    num1 *= x
                return num1
            elif num2 < 0:
                num1 = 1
                for i in range(abs(num2)):
                    num1 /= x
                return num1

    except ValueError:
        return 0


# Python 3 program to print GP.  geometric Progression
# You cant use the inbuilt python function. Write your own function


def printGP(a, r, n):
    gp = []
    try:
        a = float(a)
        r = float(r)
        n = int(n)

        if n <= 0:
            return 0
        else:
            gp.append(a)
            for i in range(1, n):
                a *= r
                gp.append(a)
            return gp
    except ValueError:
        return 0


# Python 3 program to print AP.  arithmetic Progression
# You cant use the inbuilt python function. Write your own function


def printAP(a, d, n):
    ap = []
    try:
        a = float(a)
        d = float(d)
        n = int(n)

        if n <= 0:
            return 0
        else:
            ap.append(a)
            for i in range(1, n):
                a += d
                ap.append(a)
            return ap
    except ValueError:
        return 0

# Python 3 program to print HP.   Harmonic Progression
# You cant use the inbuilt python function. Write your own function


def printHP(a, d, n):
    hp = []
    try:
        a = float(a)
        d = float(d)
        n = int(n)

        if n <= 0:
            return 0
        else:
            hp.append(1/a)
            for i in range(1, n):
                a += d
                hp.append(1/a)
            return hp
    except ValueError:
        return 0
