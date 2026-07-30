# Write a program to find sum of digits of a number.

def sumOfDigit(num):
    sum =0
    i=1
    while(num>0):
        digit = num% 10
        sum = sum + digit
        num = num //10

    return sum

n = int(input('enter a number:'))
result =sumOfDigit(n)
print('the sum of digit of number is:',result)



 