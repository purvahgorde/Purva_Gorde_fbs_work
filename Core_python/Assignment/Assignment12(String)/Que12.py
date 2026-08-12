# Python Program to count number of lowercase characters in a string.

str = input('enter the string:')
count =0

# for ch in str:
#     if chr(97) <= ch <= chr(122): #chr(97) ='a'
#         count += 1

for ch in str:
    if 'a' <= ch <= 'z': #chr(97) ='a'
        count += 1
print(count)
