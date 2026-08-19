# Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).

di ={}
n =5
def numbers(di,n):
    for i in range(1,n+1):
        di[i] = i * i
    print(di)

numbers(di,n)
