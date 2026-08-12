# Python Program to replace every blank space with hyphen in a string.
str = input('enter the String:')
str2 =''

for ch in str:
    if(ch ==' '):
        str2 += '-'
    else:
        str2 += ch

print(str2)
