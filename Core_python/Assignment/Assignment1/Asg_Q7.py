# Program to Find the Roots of a Quadratic Equation
import math
a =int(input('enter value of a '))
b =int(input('enter value of b '))
c =int(input('enter value of c '))

D =b**2 -(4 * a* c)
print(D)

root1 = (-b + math.sqrt(D))/2 * a
root2 = (-b - math.sqrt(D))/2 * a

print(f'the roots of Quadratic equation is {root1} and {root2}')