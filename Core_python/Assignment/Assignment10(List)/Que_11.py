# Write a program to print all numbers which are divisible by m and n in the
# list.

a = int(input('enter a number:'))
li =[] 
for i in range(0,a):
    num = int(input('enter a num:'))
    li.append(num)

m =int(input('enter the value of m:'))
n =int(input('enter the value of n:'))



for i in range(0,a):
    if(li[i] % m ==0 and li[i] % n ==0):
        print(li[i],end=' ')
    