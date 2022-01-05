import math


class simp:
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
        elif operator == '-':
            return self.sub()
        elif operator == '*':
            return self.multi()
        elif operator == '/':
            return self.div()


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

    # This function gives the exponent power of a number
    def exponent(self):
        return self.x ** self.y

    # This function gives the log of a number
    def log(self):
        return math.log(int(self.x))

    # Operation Type
    def decision(self, operator):
        if operator == '+':
            return self.add()
        elif operator == '-':
            return self.sub()
        elif operator == '*':
            return self.multi()
        elif operator == '/':
            return self.div()
        elif operator == '^':
            return self.exponent()

    def str_decision(self, str_operator):
        if str_operator == 'log':
            return self.add()
