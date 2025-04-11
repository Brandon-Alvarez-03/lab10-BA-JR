#Brandon Alvarez Repo - Partner 1 - https://github.com/Brandon-Alvarez-03/lab10-BA-JR
#BAlvarez Github Link and UF Email: https://github.com/Brandon-Alvarez-03
#brandon.alvarez@ufl.edu

#Jonathan Reyes Repo - Partner 2
#JReyes Github Link and UF Email: jreyes2@ufl.edu, https://github.com/nahtanoJ-dot-exe



#calculator.py
#- Defines functions used to create a simple calculator

#One function per operation, in order.

# https://github.com/Brandon-Alvarez-03/lab10-BA-JR
# Partner 1: Brandon Andrew Alvarez
# Partner 2: Jonathan Reyes

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid arguments for logarithm")
    return math.log(b, a)

def exp(a, b):
    return a ** b


