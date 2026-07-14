import random
user_id = input('enter user_id:')
passward = input('enter passward:')

if(user_id == 'Admin' and passward =='Admin@123'):
    captch =random.randint(1000,9999)
    print(f'your captch = {captch}')
    chuser = int(input('enter captch:'))
    if(chuser == captch):
        print('user login sucessfully')
    else:
        print('Invalid captch')

else:
    print('Invalid User')