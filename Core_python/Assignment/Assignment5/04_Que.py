# WAP to print Armstrong number within a given range
start = int(input('enter a starting number:'))
end = int(input('enter the end number:'))

for num in range(start , end+1):
    temp =num
    sum =0
    length = len(str(num))

    while(temp >0):
        digit = temp %10
        sum = sum + digit ** length
        temp = temp //10

    if(sum == num):
        print(num)