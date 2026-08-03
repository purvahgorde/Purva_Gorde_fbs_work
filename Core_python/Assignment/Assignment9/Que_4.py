# Write a program to find sum of n numbers using recursion.
def sum(num):
    if(num > 0):
        return num + sum(num -1)
    else:
        return 0

n = 5
res = sum(n)
print('The sum is:',res)