# Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

li =[10,20,20,50,40,67,80,80,30,20]

def element(num,li):
    count =0
    for i in range(0,len(li)):
        if(li[i] == num):
            count +=1
    if(count >0):
        return True,count
    else:
        return False,count

num = int(input('enter a number:'))
res,count = element(num,li)
print(f'The element is present {res} and count is {count}')
