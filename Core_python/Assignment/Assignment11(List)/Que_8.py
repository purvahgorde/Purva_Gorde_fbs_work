# Print 1 to 100 in snakes and ladder pattern.

# start =1,end =10
num  =1  # num=100
for i in range(10):
    row =[]
    for j in range(10):
        row.append(num)
        num +=1  # num -=1
    if(i % 2 !=0):
        row.reverse()
    print(row)
        

