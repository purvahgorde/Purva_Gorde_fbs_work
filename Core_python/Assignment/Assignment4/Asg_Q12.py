# 12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

num =int(input('enter a number:'))
length = len(str(num))
print(length)
temp = num 
sum = 0
# count =0

# while(temp > 0):
#     count +=1
#     temp = temp //10


while(temp != 0):
    digit = temp % 10
    sum = sum +(digit ** length )
    temp = temp // 10
print(sum)
if(sum == num):
    print('num is Armstrong number')
else:
    print('not Armstrong number')


