def sod(n):
    if(n > 0):
        digit = n% 10
        return digit + sod(n//10)
    else:
        return 0

n= 1234
res = sod(n)
print(res)


