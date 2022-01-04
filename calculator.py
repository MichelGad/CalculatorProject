
# Import the classes and functions from the main file
import main as mn

# Select Calculator Type
print('**************************')
print("Select calculator type.")
print('1.Simple')
print('2.Advanced')
print('3.Scientific')
print('**************************')

# take input from the user
choice = input('Enter your choice(1/2/3): ')

# Simple Calculator
if choice == '1':
    print('Simple Calculator')
    print('**************************')
    print('Select operation.')
    print('1.Add')
    print('2.Subtract')
    print('3.Multiply')
    print('4.Divide')
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
            quit = input('Do you want to close the calculator? (y/n): ')
            if quit == 'n':
                break
    else:
        print("Invalid Input")

# Advanced Calculator
if choice == '2':
    calculation = input("Enter your calculation: ")

    # Import Numbers into Variables
    x = int(calculation[0])
    y = int(calculation[2])

    # Import the operation type
    operation = calculation[1]

    adv= mn.advanced(x, y)
    result= adv.operator(operation)
    print(x, operation, y, '=', result)

    while True:
        x = result
        next_step = input("Next Step: ")
        y = int(next_step[1])
        # Import the operation type
        operation = next_step[0]
        adv = mn.advanced(x, y)
        result = adv.operator(operation)
        print(x, operation, y, '=', result)