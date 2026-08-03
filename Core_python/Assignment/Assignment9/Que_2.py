# Write a program to check if given number is Armstrong or not using recursive function.
def count(n):
    return len(str(n))

def armstrong(n):
    if(n > 0):
        digit = n % 10
        return digit ** count(num) + armstrong(n //10)
    else:
        return 0

num =153
# count =count(num)


if(armstrong(num) == num):
    print('Armstrong num')
else:
    print('not armstrong num')


        

    