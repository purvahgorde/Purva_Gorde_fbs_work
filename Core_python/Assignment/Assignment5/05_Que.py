# Write a program to print prime numbers between 1 to 100.

start =int(input('enter the starting number:'))
end =int(input('enter the end number:'))

for num in range(start,end):
    if(num >1):
        for i in range(2,num):
            if(num % i ==0):
                break
        else:
            print(num)
    else:
        print(f'{num} is nither prime nor composite')
