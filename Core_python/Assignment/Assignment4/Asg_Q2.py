# WAP to print all odd numbers until n.
n = int(input('enter a number:'))
# i =1 
# while(i < n):
#     if(i % 2 != 0):
#         print(i)
#     i += 1

for i in range(1, n):
    if(i % 2 !=0):
        print(i)