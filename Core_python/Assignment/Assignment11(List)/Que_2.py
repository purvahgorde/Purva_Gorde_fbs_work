# 2. Python Program to Merge Two Lists and Sort it
li1 =[2,5,1,4]
li2 =[3,9,8,6]
li =[]

def merge(li1,li2):
    for i in li1:
        li.append(i)

    for i in li2:
        li.append(i)

    return li

def sort(li):
    for i in range(len(li)):
        for j in range(len(li) -i -1):
            if(li[j] > li[j +1]):
                li[j],li[j+1] = li[j+1],li[j]


res = merge(li1,li2)
print(f'mesrge list {res}')
sort(res)
print(f'sorted list {res}')