s1 = int(input('enter the marks of subject1:'))
s2 = int(input('enter the marks of subject2:'))
s3 = int(input('enter the marks of subject3:'))
s4 = int(input('enter the marks of subject4:'))
s5 = int(input('enter the marks of subject5:'))

per = (s1 + s2 + s3 + s4+ s5)/500 * 100
print(per)
if(per >85):
    print('first class')
else:
    if(per >75 and per <85):
        print('second class')
    else:
        if(per > 65 and per< 75):
            print('third class')
        else:
            if(per >55 and per < 65 ):
                print('fourth class')
            else:
                if(per > 45 and per< 55):
                    print('fifth class')
                else:
                    if(per > 35 and per <45):
                        print('sixth class')
                    else:
                        if(per < 35):
                            print('you are failed')
                    
