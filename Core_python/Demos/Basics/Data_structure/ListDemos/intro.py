# 1 structured :- Denoted by []
li =[10,20,30,40]
print(type(li))

# 2 Type of data: Hetrogenous
li =[10,3.14,'abc']
print(li)

# 3 sequenced :- ordered


# 4 changable:- Mutable
print(id(li))
li[1] = 7.89
print(id(li))
print(li)

# 5 duplicat  Allowed
li =[10,20,10,10,30,20]
print(li)