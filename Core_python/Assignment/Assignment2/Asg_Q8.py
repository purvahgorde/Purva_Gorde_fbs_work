# Write a program to swap two numbers using third variable.

num1 = int(input('enter num1 '))
num2 = int(input('enter num2 '))

print(f'before swaping num1 = {num1} and num2 = {num2}')

temp =0
temp = num1
num1 = num2 
num2 =  temp

print(f'after swaping num1 = {num1} and num2 = {num2}')

