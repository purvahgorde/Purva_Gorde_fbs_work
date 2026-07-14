s1 = int(input('enter side1:'))
s2 = int(input('enter side2:'))
s3 = int(input('enter side3:'))

if(s1+s2 > s3 and s2+s3 >s1 and s1+s3 >s2 ):
    print('trangle is valid')
else:
    print('triangle is not valid')