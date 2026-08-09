# Write a program to remove duplicates from the list.

def removeDuplicate(li):
    new = []

    for ele in li:
        count = 0

        for i in new:
            if ele == i:
                count = 1
                break

        if count == 0:
            new += [ele]

    return new


li =[10,20,20,30,40,50,50,66,80]
print(li)
res = removeDuplicate(li)
print(res)



















    

