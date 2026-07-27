# Write a program to find sum of digits of a number.

def sumOfDigit(num):
    sum =0
    i=1
    while(i <= num):
        digit = num% 10
        sum = sum + digit
        num = num //10
    i+=1
    return sum

result =sumOfDigit(151)
print('the sum of digit of number is:',result)



 