start = int(input('enter a starting number:'))
end = int(input('enter the end number:'))
print(f'the prime num from {start} to {end}  ')
for num in range(start,end):
    if(num > 1):
        for i in range(2,num):
            if(num % i ==0):
                break
        else:
            print(num)
    else:
        print(f'{num} the num is nither prime nor composite')