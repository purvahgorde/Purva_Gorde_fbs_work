# 3. Python Program to Sort the List According to the Second Element in Sublist
li =[[2,3],[4,1],[8,9],[7,6]]

def sort(li):
    for i in range(len(li)):
        for j in range(len(li) -i -1):
            if(li[j][1] > li[j+1][1]):
                li[j],li[j+1] = li[j+1],li[j]

sort(li)
print(li)