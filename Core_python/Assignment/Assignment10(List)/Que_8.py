# Write a program to create a duplicate of an existing list. It should not point to
# same list.

li1 =[10,20,30,40,50]
n = len(li1)
li2 = []

for i in range(0,n):
    # li2 +=[li1[i]]
    li2.append(li1[i])

li2[3] =60
print(li1)
print(li2)

