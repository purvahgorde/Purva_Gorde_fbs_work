# wap a program of factorial using recursive function
# 0! =1
def fact(n):
    if( n > 0):
        return n * fact(n -1)
    else:
        return 1

n =5
res = fact(n)
print(res)

# digit seprate
# sum of digit
# reverse digit