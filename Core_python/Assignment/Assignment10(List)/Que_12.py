# Write a program to create three lists of numbers, their squares
# and cubes
n = int(input('enter the count of numbers:'))
li=[]
square_li =[]
cube_li =[]
for i in range(0,n):
    num =int(input('enter the element:'))
    li.append(num)

for i in range(0,n):
    square_li.append(li[i] **2)
    cube_li.append(li[i]** 3)

print(li)
print(square_li)
print(cube_li)



