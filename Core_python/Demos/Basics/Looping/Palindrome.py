n = int(input('enter a number:'))
rev =0
original = n
while(n > 0):
    digit = n % 10
    rev = rev *10 + digit
    n = n //10

if(original == rev):
    print('palindrome')
else:
    print('not palindrome')
