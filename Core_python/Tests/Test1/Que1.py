# Write a program to find the area and perimeter of following figure (Accept the
# length, breadth and radius from user:
import math
len = int(input('enter the length of rectangle:'))
bred = int(input('enter the bredth of rectangle:'))
radius = int(input('enter the radius of circle'))

area_of_rect =len * bred
area_of_circle = (math.pi * radius **2)/2

total_area = area_of_rect +area_of_circle
print(f'total area is {total_area:.2f}')

peri_of_rect = 2*(len +bred)
peri_of_circle = math.pi +2 * radius

total_perimeter = peri_of_rect +peri_of_circle
print(f'perimeter is {total_perimeter:2f}')