# 6. Python Program to Find the Union of two Lists
li1 =[1,2,3,4]
li2 =[2,3,5,7]

union =[]
for i in range(len(li1)):
    union.append(li1[i])

# print(union)
for i in range(len(li2)):
    if(li2[i] not in union):
        union.append(li2[i])
print(union)
