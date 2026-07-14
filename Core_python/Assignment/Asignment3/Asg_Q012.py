num = int(input('enter 3 digit number:'))

if(num >=100 and num<=999):
    orginal = num
    rev = 0
    while(num >0):
        digit = num % 10
        rev = rev *10 +digit
        num = num //10

    if(orginal == rev):
        print('palindrome number')
    else:
        print('not palindrome number')
else:
    print('enter valid number')