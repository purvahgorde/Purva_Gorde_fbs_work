# 1 structure:- { } : key(customized index) and value 
di={1:'python','released':1991,'developer':'Gudio van rossum'}

# 2 hetrogenous

# 3 ordered

# 4 key:immutable ,value =mutable,dict.size mutable (we add or delect value )
di[1] ='python programming' # change the value /replace value  
di[3] = 100 # add value in last

# 5 keys :unique ,values :Duplicate Alowed
di[4] =1991 # duplicate allowed
 
print(type(di))
print(di)


# from index i.e from key we can get value but from value we cannot access index in dictonary  