li =[10,20,30,40,91,50,61,55,30]
max =li[0]
for i in range(0,len(li)):
    if(li[i] > max):
        max = li[i] # value
        max = i # index

print('maximum elemnt:',max)


