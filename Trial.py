# Import the classes and functions from the main file
import main as mn
import re

operator = ''
print('*********************************')
print('Scientific Calculator')
print('*********************************')
print('Equation Format: X operator Y')
print('*********************************')
print('Addition +       | Factorial !')
print('Subtraction -    | sin')
print('Multiplication * | cos')
print('Division /       | tan')
print('Exponent ^       | log')
print('*********************************')

calculation = input("Enter your equation: ")

for i in calculation:
    if i == '+' or i == '-' or i == '*' or i == '/' or i == '^' or i == '!':
        operator = i.strip()

    str_operator = ''.join(re.split("[^a-zA-Z]*", calculation))

    num = re.findall(r'-?\d+\.?\d*', calculation)

    if operator == '+':
        x = float(num[0])
        y = float(num[1])
        sci = mn.scientific(x, y)
        result = sci.decision(operator)
        print(x, operator, y, '=', result)

    if operator == '-':
        x = float(num[0])
        y = float(num[1])
        sci = mn.scientific(x, y)
        result = sci.decision(operator)
        print(x, operator, y, '=', result)

    if operator == '*':
        x = float(num[0])
        y = float(num[1])
        sci = mn.scientific(x, y)
        result = sci.decision(operator)
        print(x, operator, y, '=', result)

    if operator == '/':
        x = float(num[0])
        y = float(num[1])
        sci = mn.scientific(x, y)
        result = sci.decision(operator)
        print(x, operator, y, '=', result)

    if operator == '^':
        x = float(num[0])
        y = float(num[1])
        sci = mn.scientific(x, y)
        result = sci.decision(operator)
        print(x, operator, y, '=', result)

    if str_operator == 'cos':
        x = float(num[0])
        sci = mn.new_scientific(x)
        result = sci.str_decision(str_operator)
        print(str_operator, x, '=', result)

    if str_operator == 'sin':
        x = float(num[0])
        sci = mn.new_scientific(x)
        result = sci.str_decision(str_operator)
        print(str_operator, x, '=', result)

    if str_operator == 'tan':
        x = float(num[0])
        sci = mn.new_scientific(x)
        result = sci.str_decision(str_operator)
        print(str_operator, x, '=', result)

    if str_operator == 'log':
        x = float(num[0])
        sci = mn.new_scientific(x)
        result = sci.str_decision(str_operator)
        print(str_operator, x, '=', result)

    if operator == '!':
        str_operator = operator
        x = int(num[0])
        sci = mn.new_scientific(x)
        result = sci.str_decision(str_operator)
        print(str_operator, x, '=', result)

    # check if user wants another calculation
    # break the while loop if answer is no
    print('If you want to quit: Write(q)')
    x = result
    next_step = input('Next Step: ')
    if next_step == 'q':
        break
    else:
        for f in next_step:
            if f == '+' or f == '-' or f == '*' or f == '/':
                operator = f.strip()

        num = re.findall(r'-?\d+\.?\d*', next_step)
        x = result
        y = float(num[0])
