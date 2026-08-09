# Write a program to remove all occurrences of a given element in the list.
def removeOccrance(li,element):
    li1=[]
    for i in li:
        if(i!= element):
            li1.append(i)

    return li1

li =[10,20,30,20,20,40,50,40,30,50]
target =20

res = removeOccrance(li,target)
print(res)

