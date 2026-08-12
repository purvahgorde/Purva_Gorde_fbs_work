def sum(n):
    if (n>0):
        return n + sum(n -1)
    else:
        return 0
    
n =5
res =sum(n)
print(res)