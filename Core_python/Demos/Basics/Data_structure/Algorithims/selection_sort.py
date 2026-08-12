def selectionSort(li):
    size=len(li)
    
    for i in range(0,size -1):
        min = i
        for j in range(i+1,size):
            if(li[j] <li[min]):
                min = j
        li[i],li[min] = li[min],li[i]
        print(li)
        print(min)

li =[40,10,60,30,50,20]
selectionSort(li)
print(li)
