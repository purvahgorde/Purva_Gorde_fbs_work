# Python Program to Remove the nth Index Character from a Non-Empty
# String
str =input('enter a string:')
n =int(input('enter the index value :'))
str2 =''

for i in range(0,len(str)):
    if(i != n):
        str2 += str[i]

print(str2)