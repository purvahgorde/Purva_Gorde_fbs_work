s1 = int(input('enter side1:'))
s2 = int(input('enter side2:'))
s3 = int(input('enter side3:'))

if(s1 == s2 == s3):
    print('it is equliteral triangle')
elif(s1==s2 or s2==s3 or s1==s3):
    print('it is isoscales triangle')
else:
    print('it is scalen triangle')