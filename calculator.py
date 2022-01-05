
# Import the classes and functions from the main file
import main as mn

# Select Calculator Type
print('**************************')
print("Select calculator type.")
print('1.Basic')
print('2.Advanced')
print('3.Scientific')
print('**************************')

# take input from the user
choice = input('Enter your choice(1/2/3): ')

# Simple Calculator
if choice == '1':
    print('**************************')
    print('Basic Calculator')
    print('**************************')
    print('Select operation.')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    print('**************************')

    # check if choice is one of the four options
    choice = input('Enter choice(1/2/3/4): ')

    while True:

        # check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            x = float(input('Enter first number: '))
            y = float(input('Enter second number: '))
            obj= mn.simp(x,y)

            if choice == '1':
                print(x, '+', y, '=', obj.add())

            elif choice == '2':
                print(x, '-', y, '=', obj.sub())

            elif choice == '3':
                print(x, '*', y, '=', obj.multi())

            elif choice == '4':
                print(x, '/', y, '=', obj.div())

            # check if user wants another calculation
            # break the while loop if answer is no
            quit = input('Do you want to quit the calculator? (y/n): ')
            if quit == 'y':
                break
    else:
        print("Invalid Input")

# Advanced Calculator
if choice == '2':
    operator = ''
    print('**************************')
    print('Advanced Calculator')
    print('**************************')
    print('Equation Format: X operator Y')
    print('**************************')
    print('Addition +')
    print('Subtraction -')
    print('Multiplication *')
    print('Division /')
    print('**************************')

    while True:

        calculation = input("Enter your equation: ")

        for num in calculation:
            if num == '+' or num == '-' or num == '*' or num == '/' or num == '^':
                operator = num.strip()
                break

        if operator == '+':
            split_calculation = calculation.split('+', 1)
            x = float(split_calculation[0])
            y = float(split_calculation[1])
            adv = mn.advanced(x, y)
            result = adv.decision(operator)
            print(x, operator, y, '=', result)

        if operator == '-':
            split_calculation = calculation.split('-', 1)
            x = float(split_calculation[0])
            y = float(split_calculation[1])
            adv = mn.advanced(x, y)
            result = adv.decision(operator)
            print(x, operator, y, '=', result)

        if operator == '*':
            split_calculation = calculation.split('*', 1)
            x = float(split_calculation[0])
            y = float(split_calculation[1])
            adv = mn.advanced(x, y)
            result = adv.decision(operator)
            print(x, operator, y, '=', result)

        if operator == '/':
            split_calculation = calculation.split('/', 1)
            x = float(split_calculation[0])
            y = float(split_calculation[1])
            adv = mn.advanced(x, y)
            result = adv.decision(operator)
            print(x, operator, y, '=', result)

        # check if user wants another calculation
        # break the while loop if answer is no
        quit = input('Do you want to quit the calculator? (y/n): ')
        if quit == 'y':
            break
    else:
        print("Invalid Input")

# Scientific Calculator
if choice == '3':
    operator = ''
    print('**************************')
    print('Scientific Calculator')
    print('**************************')
    print('Equation Format: X operator Y')
    print('**************************')
    print('Addition +')
    print('Subtraction -')
    print('Multiplication *')
    print('Division /')
    print('Exponent ^')
    print('tan')
    print('sin')
    print('cos')
    print ('Factorial')
    print('log')
    print('**************************')

    while True:

        calculation = input("Enter your equation: ")

        for num in calculation:
            if num == '+' or num == '-' or num == '*' or num == '/' or num == '^':
                operator = num.strip()
                break

        if operator == '+':
            split_calculation = calculation.split('+', 1)
            x = float(split_calculation[0])
            y = float(split_calculation[1])
            adv = mn.advanced(x, y)
            result = adv.decision(operator)
            print(x, operator, y, '=', result)

        if operator == '-':
            split_calculation = calculation.split('-', 1)
            x = float(split_calculation[0])
            y = float(split_calculation[1])
            adv = mn.advanced(x, y)
            result = adv.decision(operator)
            print(x, operator, y, '=', result)

        if operator == '*':
            split_calculation = calculation.split('*', 1)
            x = float(split_calculation[0])
            y = float(split_calculation[1])
            adv = mn.advanced(x, y)
            result = adv.decision(operator)
            print(x, operator, y, '=', result)

        if operator == '/':
            split_calculation = calculation.split('/', 1)
            x = float(split_calculation[0])
            y = float(split_calculation[1])
            adv = mn.advanced(x, y)
            result = adv.decision(operator)
            print(x, operator, y, '=', result)

        if operator == '^':
            split_calculation = calculation.split('^', 1)
            x = float(split_calculation[0])
            y = float(split_calculation[1])
            adv = mn.advanced(x, y)
            result = adv.decision(operator)
            print(x, operator, y, '=', result)

        if operator == 'log':
            split_calculation = calculation.split('log', 1)
            x = float(split_calculation[0])
            adv = mn.advanced(x)
            result = adv.decision(operator)
            print(operator, x, '=', result)

        # check if user wants another calculation
        # break the while loop if answer is no
        quit = input('Do you want to quit the calculator? (y/n): ')
        if quit == 'y':
            break
    else:
        print("Invalid Input")