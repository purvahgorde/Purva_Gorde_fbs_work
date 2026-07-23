num = int(input('enter the number:'))

if(num >=0):
    if(num >50):
        if(num >100):
            if(num > 150):
                if(num>250):
                    print('num is >250')
                else:
                    print('num > 150  but <250') 
            else:
                print('num >100 but < 150')
        else:
            print('num >50 but < 100')
    else:
        print('num is betn 0 to 50')
    
else:
    print('num is less than 0')
