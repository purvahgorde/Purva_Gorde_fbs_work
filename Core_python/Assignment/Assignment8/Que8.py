# Write a program find reverse of a number

def reverseNum(num):
    rev =0
    while(num>0):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev
n =int(input('enter the number:'))
result = reverseNum(n)
print('the reverse number is:',result)