# Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
def sum(n):
    sum=0
    for i in range(1,n+1):
        sum =sum +i
    return(sum)
result = sum(5)
print('the sum is',result)



# b. 1!+ 2! + 3! + 4!+..... + n!

def factorial(n):
    fact =1
    i =1
    while(i<=n):
        fact = fact * i
        i += 1
    return(fact)

n=int(input('enter a number:'))
sum=0
i=1
while(i<=n):
    sum =sum+ factorial(i)
    i += 1

# result =factorial(5)
# print(f'the factorial is {result}')  it print factorial of number
print('the sum is:',sum)



# c. 1^1 + 2^2 + 3^3+ ...... n^n
def exponential(n):
    sum =0
    i =1
    while(i <= n):
        sum = sum + (i ** i)
        i += 1
    return sum

result=exponential(5)
print('the sum of exponential is :',result)
