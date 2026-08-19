# Write a Python program to find all the anagrams and group them
# together from a given list of strings.

words =["eat","tea","tan","nat","bat","ate"]

groups ={}

for i in words:
    key =''.join(sorted(i))  #'-'.join(['a', 'e', 't']) =>"a-e-t"
                            
    if key not in groups:
        groups[key] =[]  #create empty list

    groups[key].append(i) 

print(groups.values()) 


# key =''.join(sorted(i))
# i = "eat"

# sorted(i)
#    ↓
# ['a', 'e', 't']

# ''.join(...)
#    ↓
# "aet"

# key = "aet"