a1 = int(input('enter age of person 1:'))
t1 = int(input('enter tickect price :'))
total_price = 0
if(a1 <12):
    total_price = total_price +(t1 * 0.3)
elif(a1>59):
    total_price = total_price +(t1 * 0.50)
else:
    total_price =total_price +t1
print(total_price)
a2 = int(input('enter age of person 2:'))
t2 = int(input('enter tickect price :'))

if(a2 <12):
    total_price = total_price +(t2 * 0.3)
elif(a2>59):
    total_price = total_price +(t2 * 0.50)
else:
    total_price =total_price +t2
print(total_price)
a3 = int(input('enter age of person 3:'))
t3 = int(input('enter tickect price :'))

if(a3 <12):
    total_price = total_price +(t3 * 0.3)
elif(a3>59):
    total_price = total_price +(t3 * 0.50)
else:
    total_price =total_price +t3
print(total_price)
a4 = int(input('enter age of person 4:'))
t4 = int(input('enter tickect price :'))

if(a4 <12):
    total_price = total_price +(t4 * 0.3)
elif(a4>59):
    total_price = total_price +(t4 * 0.50)
else:
    total_price =total_price +t4
print(total_price)
a5 = int(input('enter age of person 5:'))
t5 = int(input('enter tickect price :'))

if(a5 <12):
    total_price = total_price +(t5 * 0.3)
elif(a5>59):
    total_price = total_price +(t5 * 0.50)
else:
    total_price =total_price +t5

print(f'total price became {total_price}')