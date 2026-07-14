units = int(input('enter units:'))

bill =0
if(units<=50):
    bill =units * 0.50
elif(units <=150):
    bill = (50 * 0.50) + (units - 50) * 0.75
elif(units<=250):
    bill =(50 * 0.50) +(100 * 0.75 )+ (units - 150)* 1.20 

print('total electricity bill is ',bill)