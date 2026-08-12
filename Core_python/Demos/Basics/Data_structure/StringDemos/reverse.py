str =input('enter the string:')
rev =''
# 1st logic
for i in range(len(str) -1,-1,-1):
    rev = rev+ str[i]

print(rev)

# 2nd logic
for i in str:
    rev= i+rev 
print(rev)

# rev = i +rev
#       p +" "
#       up
#       rup
#       vrup
#       avrup
