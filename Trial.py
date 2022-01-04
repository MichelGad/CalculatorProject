calculation = input("Enter your calculation: ")

x = ''
operator = ''
y= ''
for num in calculation:
    if num.isdigit():
        x += num
    if num == '+' or num == '-' or num =='*' or num == '/':
        operator=num.strip()
        break
    if num == '+' or num == '-' or num =='*' or num == '/':
        y=num.strip()

print(x)