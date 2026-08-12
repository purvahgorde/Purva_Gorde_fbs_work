# Python Program to count number of digits and letters in a string.

str = input('enter the string:')
word_count =1
char =0
for ch in str:
    char +=1
    if(ch ==' '):
        word_count +=1
        char -=1
print(char)
print(word_count)


