def series(n):
    if(n>0): # condition is use for stop the infinite function calling
        print(n)
        series(n-1)
n = 5
series(n)