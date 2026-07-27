# Write a program find reverse of a number

def reverseNum(num):
    rev =0
    i =1
    while(i <= num):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev

result = reverseNum(1234)
print('the reverse number is:',result)