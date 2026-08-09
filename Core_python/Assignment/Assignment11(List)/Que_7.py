# 7. Python Program to Find the Intersection of Two Lists
li1 = [1,2,3,4,8,9]
li2 = [2,3,5,6,9,8]
intersection =[ ]

for i in range(len(li1)):
    for j in range(len(li2)):
        if(li1[i] == li2[j]):
            intersection.append(li1[i])

print(intersection)