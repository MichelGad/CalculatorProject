calculation = input("Enter your calculation: ")


operator = ''

for num in calculation:

    if num == '+' or num == '-' or num =='*' or num == '/' or num=='**':
        operator=num.strip()
        break

print(operator)