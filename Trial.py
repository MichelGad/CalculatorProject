# Import the classes and functions from the main file
import main as mn
import re

calculation = input("Enter your equation: ")

for i in calculation:
    if i == '+' or i == '-' or i == '*' or i == '/':
        operator = i.strip()

num = re.findall(r'-?\d+\.?\d*', calculation)
x = float(num[0])
y = float(num[1])

while True:

    if operator == '+':
        adv = mn.advanced(x, y)
        result = adv.decision(operator)
        print(x, operator, y, '=', result)

    if operator == '-':
        adv = mn.advanced(x, y)
        result = adv.decision(operator)
        print(x, operator, y, '=', result)

    if operator == '*':
        adv = mn.advanced(x, y)
        result = adv.decision(operator)
        print(x, operator, y, '=', result)

    if operator == '/':
        adv = mn.advanced(x, y)
        result = adv.decision(operator)
        print(x, operator, y, '=', result)

    # check if user wants another calculation
    # break the while loop if answer is no
    print('If you want to quit: Write(q)')
    next_step = input('Next Step: ')
    if next_step == 'q':
        break
    else:
        for i in next_step:
            if i == '+' or i == '-' or i == '*' or i == '/':
                operator = i.strip()

        num = re.findall(r'-?\d+\.?\d*', next_step)
        x = result
        y = float(num[0])

