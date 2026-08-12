# Python Program to find larger string without using built-in functions.

str1 =input('enter the String1:')
str2 = input('enter the String2:')
count1 =0
count2 =0

for ch in str1:
    count1 +=1
print(count1)

for ch in str2:
    count2 +=1
print(count2)

if(count1 > count2):
    print('larger string is',str1)
elif(count2 >count1):
    print('larger string is',str2)
else:
    print('both are equal')
