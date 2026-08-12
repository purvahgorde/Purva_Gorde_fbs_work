# Python Program to Detect if Two Strings are Anagrams
str1 ='cat'
str2 ='act'

if(len(str1) != len(str2)):
    print('not anagrem')
count1 ={}

for ch in str1:
    if ch in count1:
        count1[ch] +=1
    else:
        count1[ch] = 1

for ch in str2:
    if ch in count1:
        count1[ch] -= 1
    else:
        count1[ch] = -1

for i in count1:
    if(count1[i] !=0):
        print(False)
        break
else:
    print(True)
# print(count1)