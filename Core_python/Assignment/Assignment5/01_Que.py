# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.
for i in range(1,4):
    userid = input('enter the username:')
    passward = input('enter the passward:')
    if(userid == 'Admin' and passward =='Admin@123'):
        print('login sucessful')
        break
    else:
        if(i==3):
            print('3 attempted completed')
        else:
            print('Re-enter the credential')
    