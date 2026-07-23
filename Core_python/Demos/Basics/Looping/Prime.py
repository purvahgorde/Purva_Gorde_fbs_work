num = int(input('enter a number:'))
if(num > 1):
    for i in range(2,num//2 +1):
        print(i)
        if(num % i ==0):
            print(f'{num} is not prime number')
            break
    else:
        print(f'{num} is prime number')
else:
    print(f'{num} is not prime number')