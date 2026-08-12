# Python Program to Remove the Characters of Odd Index Values in a
# String

str = input('enter the string:')
str2 =''

for ch in range(0,len(str)):
    if( ch % 2 ==0):
        str2 =str2 + str[ch]

print(str2) 