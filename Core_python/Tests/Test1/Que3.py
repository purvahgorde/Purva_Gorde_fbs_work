# Write a program to accept distance in km and convert it into meters and
# centimeters both.

dist = int(input('enter the distance in kilometer:'))
meter = dist * 1000
cm = dist * 100000

print(f'{dist} km into {meter} m')
print(f'{dist} km into {cm} cm')