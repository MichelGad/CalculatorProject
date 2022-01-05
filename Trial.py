import main as mn

calculation = input("Enter your equation: ")

import re

num= re.findall(r'\d+(?:\.\d+)?', calculation)
# code to find characters in string
print(num)

