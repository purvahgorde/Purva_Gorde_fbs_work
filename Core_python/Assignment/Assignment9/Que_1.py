# Write a program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions
def factorial(n):
    if(n > 0):
        return n * factorial(n-1)
    else:
        return 1
# n =5

# res = factorial(n)
# print(res)

def sum(n):
    if( n > 0):
        
        return sum(n -1) + factorial(n)
    else:
        return 0
n =4 
res = sum(n)
print('the sum of the factorial is:', res)