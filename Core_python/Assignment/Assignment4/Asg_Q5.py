# WAP to print Fibonacci series upto n.
n = int(input('enter a number:'))
# i = 0
# j = 1
# while(i <= n):
#     print(i , end =" ")
#     k =i + j
#     i = j
#     j = k


i =-1
j = 1
for z in range(n):
        
        k = i + j
        print(k,end=" ")
        i = j
        j = k
        
