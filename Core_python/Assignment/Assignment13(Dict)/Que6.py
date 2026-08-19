# Python Program to Multiply All the Items in a Dictionary

di ={1:1,2:2,3:3,4:4}

def multiply(di):
    multi =1
    for i in di:
        multi =multi * di[i]
    print(multi)

multiply(di)