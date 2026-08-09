# Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.
n =int(input('enter a number of element:'))
li =[0] * n
even_li =[]
odd_li =[]
for i in range(0,n):
    num =int(input('enter a number'))
    li[i] = num

for i in range(0,n):
    if(li[i] % 2 ==0):
        even_li.append(li[i])
    else:
        odd_li.append(li[i])
print(even_li)
print(odd_li)   