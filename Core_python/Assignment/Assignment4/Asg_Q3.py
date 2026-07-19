# WAP to print sum of series upto n.
n = int(input('enter a number:'))
# i = 1
sum = 0
# while(i <= n):
#     sum = sum + i
#     print(sum)
#     i += 1

for i in range(1, n+1):
    sum = sum + i
print(sum)