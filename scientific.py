import math


# This class is used for scientific calculator operations
# It can do five simple operations with two variable
# Addition, Subtraction, Multiplication, Division and Exponentiation
# The whole equation is entered as one string (x operator y)
# Each Variable extracted using the findall function from the Regular expression operations library
# The operator is extracted using a for loop with strip function
# Using an additional input function(Next Step: operator y),
# the result from the previous equation can be used as x variable for the new equation
class scientific:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # This function adds two numbers
    def add(self):
        return self.x + self.y

    # This function subtracts two numbers
    def sub(self):
        return self.x - self.y

    # This function multiplies two numbers
    def multi(self):
        return self.x * self.y

    # This function divides two numbers
    def div(self):
        return self.x / self.y

    # This function gives the result of raising a number to a power of another number
    def exponent(self):
        return self.x ** self.y

    # Operation Type
    def decision(self, operator):
        if operator == '+':
            return self.add()
        elif operator == '_':
            return self.sub()
        elif operator == '*':
            return self.multi()
        elif operator == '/':
            return self.div()
        elif operator == '^':
            return self.exponent()


# This class is used for scientific calculator operations
# It can do five simple operations with one variable
# Sine, Cosine, Tangent, Logarithm and Factorial
# The whole equation is entered as one string (operator x)
# The variable (x) extracted using the findall function from the Regular expression operations library
# Also, The operator is extracted using the findall function from the Regular expression operations library
class new_scientific:
    def __init__(self, x):
        self.x = x

    # This function gives the cose of a number
    def cos(self):
        return math.cos(int(self.x))

    # This function gives the sine of a number
    def sin(self):
        return math.sin(int(self.x))

    # This function gives the tangent of a number
    def tan(self):
        return math.tan(int(self.x))

    # This function gives the logarithmic result of a number
    def log(self):
        return math.log(int(self.x))

    # This function gives the factorial result of a number
    def fact(self):
        return math.factorial(int(self.x))

    def str_decision(self, str_operator):
        if str_operator == 'cos':
            return self.cos()
        if str_operator == 'sin':
            return self.sin()
        if str_operator == 'tan':
            return self.tan()
        if str_operator == 'log':
            return self.log()
        if str_operator == '!':
            return self.fact()


help(scientific)
help(new_scientific)
