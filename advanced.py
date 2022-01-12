# This class is used for advanced calculator operations
# It can do four simple operations with two variable
# Addition, Subtraction, Multiplication, and Division
# The whole equation is entered as one string (x operator y)
# Each Variable extracted using the findall function from the Regular expression operations library
# The operator is extracted using a for loop with strip function
# Using an additional input function(Next Step: operator y),
# the result from the previous equation can be used as x variable for the new equation
class advanced:
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


help(advanced)
