def strongNum():
    num = int(input('enter a num:'))
    sum =0
    temp=num
    while(num >0):
        digit = num  % 10
        fact =1  # restart the fact =1
        i=1
        while(i<=digit):
            fact = fact * i
            i+=1
        sum = sum + fact
        num =num//10
    if(sum == temp):
        print('strong number')
    else:
        print('not strong number')
strongNum()