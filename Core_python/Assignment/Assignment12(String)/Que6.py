# Python Program to Take in a String and Replace Every Blank Space
# with Hyphen
str = input('enter a string:')
str2 =''

for ch in str:
    if(ch == ' '):
        str2 += '-'
    else:
        str2 +=ch

print(str2)