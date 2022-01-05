import re

calculation = input('Enter your equation: ')

num = re.findall(r'-?\d+\.?\d*', calculation)

x = float(num[0])
y = float(num[1])

print(x)
print(y)
