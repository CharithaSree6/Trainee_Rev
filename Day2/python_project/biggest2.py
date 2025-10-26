'''
date:25-10-2025
author:charitha
descrption:biggest of two numbers
'''

num1 = int(input("enter the number:"))
num2 = int(input("enter another number:"))

if num1 == num2:
    print('both numbers are equal')

elif num1 > num2:
    print(f'{num1} is greater than {num2}')
else:
    print(f'{num2} is greater than {num1}')
