# Python Program to Replace all Occurrences of ‘a’ with $ in a String

str = input('enter a string:')

# print(str.replace('a','$'))
str2 =''
for i in str:
    if(i =='a'):
        str2 += '$'
    else:
        str2 += i
print(str2)
    