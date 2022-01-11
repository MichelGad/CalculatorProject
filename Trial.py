# Import the classes and functions from the main file
import main as mn
import re

operator = ''
print('*********************************')
print('Scientific Calculator')
print('*********************************')
print('Equation Format: X operator Y')
print('*********************************')
print('Addition +       | ')
print('Subtraction -    | sin')
print('Multiplication * | cos')
print('Division /       | tan')
print('Exponent ^       | log')
print('*********************************')

while True:
    calculation = input("Enter your equation: ")

    for i in calculation:
        if i == '+' or i == '-' or i == '*' or i == '/' or i == '^' or i == '!':
            operator = i.strip()

    str_operator = ''.join(re.split("[^a-zA-Z]*", calculation))
    num = re.findall(r'-?\d+\.?\d*', calculation)

    if str_operator == 'sin' or str_operator == 'cos' or str_operator == 'tan' \
            or str_operator == 'log' or str_operator == '^':

        x = float(num[0])
        if str_operator == 'cos':
            sci = mn.new_scientific(x)
            result = sci.str_decision(str_operator)
            print(str_operator, x, '=', result)

        if str_operator == 'sin':
            sci = mn.new_scientific(x)
            result = sci.str_decision(str_operator)
            print(str_operator, x, '=', result)

        if str_operator == 'tan':
            sci = mn.new_scientific(x)
            result = sci.str_decision(str_operator)
            print(str_operator, x, '=', result)

        if str_operator == 'log':
            sci = mn.new_scientific(x)
            result = sci.str_decision(str_operator)
            print(str_operator, x, '=', result)

        quite = input('Do you want to quit this calculator? (y/n): ')
        if quite == 'y':
            break
        elif quite == 'n':
            continue
        else:
            print("Invalid Input")

    if operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == '^':

        x = float(num[0])
        y = float(num[1])

        while True:
            if operator == '+':
                sci = mn.scientific(x, y)
                result = sci.decision(operator)
                print(x, operator, y, '=', result)

            if operator == '-':
                sci = mn.scientific(x, y)
                result = sci.decision(operator)
                print(x, operator, y, '=', result)

            if operator == '*':
                sci = mn.scientific(x, y)
                result = sci.decision(operator)
                print(x, operator, y, '=', result)

            if operator == '/':
                sci = mn.scientific(x, y)
                result = sci.decision(operator)
                print(x, operator, y, '=', result)

            if operator == '^':
                sci = mn.scientific(x, y)
                result = sci.decision(operator)
                print(x, operator, y, '=', result)

            # check if user wants another calculation
            # break the while loop if answer is no
            print('If you want to quit: Write(q)')
            next_step = input('Next Step: ')
            if next_step == 'q':
                break
            else:
                for f in next_step:
                    if f == '+' or f == '-' or f == '*' or f == '/':
                        operator = f.strip()
                x = result
                num = re.findall(r'-?\d+\.?\d*', next_step)
                y = float(num[0])
