# 11. Find the area and circumference of circle.
import math
radius = int(input('enter radius of circle '))

area = math.pi * radius**2
circumference = 2 * math.pi * radius

print(f'area of circle is {area} and circumference is {circumference}')