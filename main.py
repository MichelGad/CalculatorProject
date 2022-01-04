class simp:
    def __init__(self, x, y):
        self.x= x
        self.y= y

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
        self.x= x
        self.y= y

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

    # This function gives the power of a number
    def power(self):
        return self.x ** self.y

    # Operation Type
    def decision (self, operator):
        if operator == '+':
            return self.add()
        elif operator == '-':
            return self.sub()
        elif operator == '*':
            return self.multi()
        elif operator == '/':
            return self.div()
        elif operator == '^':
            return self.power()