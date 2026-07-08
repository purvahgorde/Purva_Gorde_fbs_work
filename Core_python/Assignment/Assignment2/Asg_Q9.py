# Write a program to swap two numbers without using third variable.
num1 = int(input('enter num1 '))
num2 = int(input('enter num2 '))

print(f'before swaping num1 = {num1} and num2 = {num2}')

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f'after swaping num1 = {num1} and num2 = {num2}')
