# li=[10,20,30,40,50,60]
# # positive index start from 0 to n  
# # i.e 0 ,1, 2, 3, 4,5  left to right
# print(li[0])
# # negative index start from -1 to -n 
# # i.e -7,-6,-5,-4,-3,-2,-1 right to left
# print(li[-1])

# # subscript
# print(len(li))
# print(li[len(li) -1 ])

n = int(input('enter a number:'))
li=[0]*n

for i in range(n):
    num =int(input('enter the element'))
    li[i]+=num
print(li)

