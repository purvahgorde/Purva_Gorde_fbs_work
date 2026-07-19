# WAP to check if given number Strong Number.
# strong num = sum of factorial of num is same as given number
num = int(input('enter a number:'))
sum =0
original = num
while(num >0):
    digit = num % 10

    fact =1
    
    for i in range(1,digit +1):
        fact = fact *i

    sum = sum + fact
    num =num //10


if(sum == original):
    print('strong number')
else:
    print('not strong number')

    
