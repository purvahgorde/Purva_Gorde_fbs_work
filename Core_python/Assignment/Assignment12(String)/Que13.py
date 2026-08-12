# Python Program to count number of digits and letters in a string.

str = input('enter the string:')
count_digit =0
count_letter =0

for i in str: 
    if('0'<= i <='9'):
        count_digit +=1

    if('a'<= i <='z' or 'A' <= i <='Z'):
        count_letter +=1

print(count_digit)
print(count_letter)

