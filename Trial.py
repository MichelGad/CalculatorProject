choice = input('Enter choice(1/2/3/4): ')


# check if choice is one of the four options
if choice in ('1', '2', '3', '4'):
     x = input('Enter first number: ')
     while True:
         if x is str:
            print('invalid Input')
         else:
             break