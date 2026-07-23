gender =input('enter gender (m/f): ')
age =int(input('enter age: '))

if(gender == 'f'):
    if(age >= 18):
        print('eligible')
    else:
        print('not eligible')
else:
    if(age>=21):
        print('eligible')
    else:
        print('not eligible')