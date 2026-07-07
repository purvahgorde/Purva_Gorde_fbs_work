# 5. Write a program to enter P, T, R and calculate Compound Interest.
P = int(input('enter principal'))
T = int(input('enter time in yrs'))
R = int(input('enter rate in %'))

amount = P * (1+R/100)**T
C_I = amount - P

print('the compund interest is',C_I)
