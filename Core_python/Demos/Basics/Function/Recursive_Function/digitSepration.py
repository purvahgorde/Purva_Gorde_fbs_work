def ds(n):
    if(n>0):
        ds(n//10)
        digit = n%10
        print(digit ,end=' ')
        
n = 1234
ds(n)
