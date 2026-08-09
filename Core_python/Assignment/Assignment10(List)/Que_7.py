# Write a program to create a new list from existing list which contains cube of
# each number of list.

li1 =[1,2,3,4,5,6,7]
n = len(li1)
li2=[0] * n

for i in range(0,len(li1)):
    li2[i] = li1[i] ** 3
print(li2)


# def cubeList(li1):
#     n = len(li1)
#     li2 = [0] * n

#     for i in range(n):
#         li2[i] = li1[i] ** 3

#     return li2


# li1 = [1, 2, 3, 4, 5, 6, 7]
# result = cubeList(li1)

# print(result)