# i/p : My name is purva
# o/p : purva is name My 

str ='My name is purva'
word =''
rev =''

for i in str:
    if(i !=' '):
        word =word +i
        # print(word)
    else:
        rev = word + " " +rev
        word =""  #clear the privious word and make it empty to store next word
        # print(rev)
        # print(word)
rev = word +' '+ rev 
print(rev)