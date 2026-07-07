# Write a Program to input two angles from user and find third angle of the triangle

angle1 =int(input('enter value of angle 1 in degree '))
angle2 =int(input('enter value of angle 2 in degree '))

angle3 = 180 -(angle1 +angle2)

print(f'third angle of triangle is {angle3} degree')