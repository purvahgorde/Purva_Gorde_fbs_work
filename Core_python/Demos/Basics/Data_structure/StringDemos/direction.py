import math
path =input('enter the path:(N,E,W,S) ')
x =0
y =0
dist =0
for i in path:
    if(i =='W'):
        x =x-1
    elif(i =='E'):
        x = x+1
    elif(i == 'N'):
        y =y+1
    elif(i == 'S'):
        y =y -1
    else:
        print('invalid input')
        break
print(x)
print(y)
dist =math.sqrt(x **2 + y **2)
print(dist)
