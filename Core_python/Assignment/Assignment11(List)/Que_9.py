# 9. Write a program to create three lists of numbers, their squares and cubes
n = int(input('enter the count of number in list:'))
li=[ ]
sqrt_li =[ ]
cube_li =[ ]
for i in range(n):
    num =int(input(f'enter the element {i+1}:'))
    li.append(num)

for i in range(n):
    sqrt_li.append(li[i] **2)
    cube_li.append(li[i]**3)

print(li)
print(sqrt_li)
print(cube_li) 