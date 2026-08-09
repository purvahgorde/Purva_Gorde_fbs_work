# Write a program to find maximum and minimum element in a list.
li =[10,23,56,4,79,80]
max =li[0]
min=li[0]

for i in range(0,len(li)):
    if(li[i] >max):
        max = li[i]

    if(li[i]<min):
        min = li[i]

print(f'Maximum element is {max} and minimum element is {min}')
