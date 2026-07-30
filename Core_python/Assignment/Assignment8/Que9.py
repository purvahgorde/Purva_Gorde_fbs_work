# Write a program to check if entered number is a palindrome or not.
def palindrome(num):
    rev =0
    temp = num
    
    while(num>0):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    
    if(rev == temp):
        print('palindrome number')
    else:
        print(' not palindrome number')

n =int(input('enter a number:'))
palindrome(n)
