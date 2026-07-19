# WAP to check if given number is Perfect Number.
# perfect number = sum of all divisor of number excluding number itself
# ex num = 6   divisor of 6 = 1,2,3,6 so sum of all divisor excluding number itself i.e 1+2+3 =6
# 6 is perfect number

num = int(input('enter a number:'))
sum =0
for i in range(1,num):
    if(num % i ==0):
        sum = sum + i

if(sum == num):
        print('perfect number')
else:
        print('not perfect number')