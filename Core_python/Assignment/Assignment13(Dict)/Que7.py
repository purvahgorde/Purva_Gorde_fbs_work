# Python Program to Remove the Given Key from a Dictionary

di={1:"apple",
    2:"mango",
    3:"oranges",
    4:"grapes"
}

d2={}
key =2

def fruits(di,key):
    for i in di:
        if(i != key):
            d2[i] = di[i]

    print(d2)

fruits(di,key)

