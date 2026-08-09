# Python Program to Sort a List According to the Length of the Elements
# within the list.

li =['12456','123','6542','12']
# print(len(li[1]))

for i in range(len(li)):
    for j in range(len(li) -i -1):
        if(len(li[j]) > len(li[j+1])):
            li[j],li[j+1] = li[j+1],li[j]

print(li)