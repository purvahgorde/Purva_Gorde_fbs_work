# 10. Write a program to print list after removing even numbers.
n =int(input('enter the count of numbers in list:'))
li=[]
odd_li =[]

for i in range(n):
    num = int(input('enter the element in list:'))
    li.append(num)

for i in range(n):
    if(li[i]% 2!=0):
        odd_li.append(li[i])

print(li)
print(odd_li)