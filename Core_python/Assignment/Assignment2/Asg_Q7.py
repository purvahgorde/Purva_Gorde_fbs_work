# Find the sum of three-digit number.

num = int(input('enter three-degit  number '))
sum =0
while(num>0):
    digit = num % 10
    sum = sum + digit
    num = num //10

print(f'sum of three_digit number {sum}')