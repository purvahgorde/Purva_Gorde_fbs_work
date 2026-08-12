# select only those value which pass the condition 
# it give output in True or false 

data = [1,2,3,4,5,6,7,8,9,10]

res = list(filter(lambda num: num % 2 == 0, data))

print(res)

# it is 2nd example of filter
# it also accept the any return value and convert into boolean
# 0,0.0,'',[],{} => return False 
# and any non zero number, string,value return =>True 

data = [1,2,3,4,5,6,7,8,9,10]

res = list(filter(lambda num:num * num,data ))
print(res)


