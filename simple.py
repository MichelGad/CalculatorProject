# This class is used for simple calculator operations
# It can only do four simple operations with two variable (x,y)
# Addition, Subtraction, Multiplication, and Division
# Each Variable is imported using a separate input function
class simple:
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


help(simple)
