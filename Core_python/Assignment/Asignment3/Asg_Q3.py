angle1 = int(input('enter value of angle1:'))
angle2 = int(input('enter value of angle2:'))
angle3 = int(input('enter value of angle3:'))

sum = angle1 + angle2 + angle3

if(sum == 180):
    print('triangle is valid')
else:
    print('triangle is not valid')