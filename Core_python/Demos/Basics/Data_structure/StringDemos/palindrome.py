str = 'madam'
rev =''

for i in range(len(str)-1,-1,-1):
    rev = rev + str[i]

if (str == rev):
    print(True)
else:
    print(False)