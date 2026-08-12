li = [10,99,40,95,70,90]

max =li[0]
sec_max = -1

for i in range(0,len(li)):
    if( li[i] > max):
        sec_max =max
        max = li[i]

    elif(li[i] > sec_max and li[i]!= max):
        sec_max = li[i]

print(sec_max)



        