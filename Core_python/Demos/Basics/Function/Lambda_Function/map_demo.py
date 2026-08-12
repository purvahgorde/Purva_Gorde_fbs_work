# map() gives every element of an iterable such as list 
# it return output in object  

data =[1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda num :num * num,data))
print(res)