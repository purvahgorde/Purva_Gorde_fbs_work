# to pass multiple value to function
# Mention astrick(*) symbol before parameter name in function defination
# value store in tuple format
# use for loop to assces the value individually

def add(*num):
    sum=0
    for i in num:
        sum = sum+i
    return sum
    

res =add(10,20,30,40)
print('Addition is :',res)