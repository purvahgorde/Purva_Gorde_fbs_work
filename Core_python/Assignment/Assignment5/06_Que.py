# Write a program to print first n prime numbers.
n =int(input('enter the number:'))
num=2
while(n >0):
    count =0
    for i in range(1,num+1):
        if(num % i ==0):
            count+=1
    if(count ==2):
        print(num)
        n -= 1
    num += 1
    
    
