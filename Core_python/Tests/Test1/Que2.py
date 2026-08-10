# 2. Write a program to calculate simple interest based on Principal, Rate and Time
# (SI = P*R*T/100)
principal =int(input('enter the principal value:'))
rate = int(input('enter the rate :'))
time = int(input('enter the time in yrs:'))

S_I = (principal * rate * time)/100

print(S_I)