# Write a program to find factorial using recursion.

def fact(n):
    if(n >0):
        return n * fact(n-1)
    else:
        return 1

n = 6
res = fact(n)
print('The Factorial is :',res)