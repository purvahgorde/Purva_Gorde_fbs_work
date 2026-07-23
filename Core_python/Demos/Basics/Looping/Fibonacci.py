n = int(input('enter a number:'))
a = -1
b = 1

for i in range(n):
    c = a + b
    print(c)
    a = b
    b = c