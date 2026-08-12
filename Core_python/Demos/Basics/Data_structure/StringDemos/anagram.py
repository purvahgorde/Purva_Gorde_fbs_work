str1 ='cat'
str2 ='act'

if(len(str1) != len(str2)):
    print('not anagrem')
count1 ={}
count2 ={}

for ch in str1:
    if ch in count1:
        count1[ch] +=1
    else:
        count1[ch] =1

for ch in str2:
    if ch in count2:
        count2[ch] +=1
    else:
        count2[ch] =1

if(count1 == count2):
    print(True)
else:
    print(False)