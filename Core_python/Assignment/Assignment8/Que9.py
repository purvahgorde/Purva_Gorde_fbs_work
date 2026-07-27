# Write a program to check if entered number is a palindrome or not.
def palindrome(num):
    rev =0
    temp = num
    i =1
    while(i <= num):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    i += 1
    if(rev == temp):
        print('palindrome number')
    else:
        print(' not palindrome number')

palindrome(12321)
