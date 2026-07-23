# 7. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
n = int(input('enter the number:'))
fact =1
sum =0
for i in range(1,n + 1):
    fact = fact * i
    sum = sum +fact
print(f'Sum = {sum}')

# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
N = int(input('enter the number:'))
sum =0
for i in range(1,N+1):
    sum = sum + (N ** i)
print(f'sum is {sum}')

# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int(input('enter the number:'))
sum =0
for i in range(n):
    sum =sum +(2 ** i)
print(f'sum is {sum}')

# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
a = int(input('enter the number:'))
sum =0
for i in range(1,a+1):
    sum =sum +(a ** i)/i
print(f'sum is {sum}')

# e. x - x2/3 + x3/5 - x4/7 + .... to n terms
x = int(input('enter the number:'))
n = int(input('enter the ending value:'))
den =1
sum =0
sign=1

for i in range(1,n+1):
    sum = sum +sign*(x**i)/den
    den+=2
    sign*=-1

   
print(f'sum is {sum}')