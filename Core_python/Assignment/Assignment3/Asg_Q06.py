SP = int(input('enter selling price:'))
CP = int(input('enter cost price:'))

if(SP > CP):
    print('profit')
elif(SP < CP):
    print('loss')
else:
    print('no profit no loss')