# Python Program to count the occurrences of ach word in a string.
str ="purvaaaaa"
d1 ={}

for i in str:
    if(i in d1):
        d1[i] += 1
    else:
        d1[i] =1
        
print(d1)