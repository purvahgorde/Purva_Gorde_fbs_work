# WAP to print factorial of a number .
num = int(input('enter a number:'))
# i =1 
fact = 1
# while(i <= num):
#     fact = fact * i
#     print(fact )
#     i += 1

for i in range(1, num + 1):
    fact = fact * i

print(fact)