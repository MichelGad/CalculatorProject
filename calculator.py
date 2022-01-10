# Import the classes and functions from the main file
import main as mn
import re

while True:
    # Select Calculator Type
    print('*********************************')
    print("Select calculator type.")
    print('1.Basic')
    print('2.Advanced')
    print('3.Scientific')
    print('Or q.Quit')
    print('*********************************')

    # take input from the user
    while True:
        choice = input('Enter your choice(1/2/3/q): ')
        if choice in ('1', '2', '3', 'q'):
            break
        else:
            print("Invalid Input")

    # Simple Calculator
    if choice == '1':
        while True:
            print('*********************************')
            print('Basic Calculator')
            print('*********************************')
            print('Select operation.')
            print('1.Addition')
            print('2.Subtraction')
            print('3.Multiplication')
            print('4.Division')
            print('*********************************')

            # check if choice is one of the four options
            choice = input('Enter choice(1/2/3/4): ')

            # check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):
                x = float(input('Enter first number: '))
                y = float(input('Enter second number: '))
                obj = mn.simp(x, y)

                if choice == '1':
                    print(x, '+', y, '=', obj.add())

                elif choice == '2':
                    print(x, '-', y, '=', obj.sub())

                elif choice == '3':
                    print(x, '*', y, '=', obj.multi())

                elif choice == '4':
                    print(x, '/', y, '=', obj.div())

            else:
                print("Invalid Input")
                continue

                # check if user wants another calculation
                # break the while loop if answer is no
            quite = input('Do you want to quit this calculator? (y/n): ')
            if quite == 'y':
                break
            elif quite == 'n':
                continue
            else:
                print("Invalid Input")

    # Advanced Calculator
    if choice == '2':
        operator = ''
        print('*********************************')
        print('Advanced Calculator')
        print('*********************************')
        print('Equation Format: X operator Y')
        print('*********************************')
        print('Addition +')
        print('Subtraction -')
        print('Multiplication *')
        print('Division /')
        print('*********************************')

        while True:

            calculation = input("Enter your equation: ")

            for i in calculation:
                if i == '+' or i == '-' or i == '*' or i == '/':
                    operator = i.strip()

            num = re.findall(r'-?\d+\.?\d*', calculation)
            x = float(num[0])
            y = float(num[1])

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

    # Scientific Calculator
    if choice == '3':
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

        while True:

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

    if choice == 'q':
        break
