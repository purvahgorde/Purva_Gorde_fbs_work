# Write a program to find sum of digits using recursion.
def sum_of_digit(n):
    if(n >0):
        digit =n % 10
        return digit +sum_of_digit(n //10)
    else:
        return 0
n =123456
res = sum_of_digit(n)
print('The sum of digit is :',res)