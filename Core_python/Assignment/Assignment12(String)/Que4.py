# Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

str = input('enter the String:')
str2 =''

for ch in range(0,len(str)):
    if(ch ==0 ):
        str2 =str2 + str[len(str) -1]  
#               " "+"a"
    elif(ch ==len(str)-1):
        str2 =str2+str[0]
#             " "+"p"
    else:
        str2 = str2+str[ch]
#               " "+"urv"
print(str2)
