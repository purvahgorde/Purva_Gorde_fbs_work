# Python Program to Check if a Given Key Exists in a Dictionary or Not

di ={1:"apple",2:"mango",3:"oranges",4:"grapes"}
key =int(input("enter the key:"))
def fruits(di,key):
    for i in di:
        if i == key:   # di[i]=values and i=keys
            return True
    else:
        return False

res =fruits(di,key)
print(res)