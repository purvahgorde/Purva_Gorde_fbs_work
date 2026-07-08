# Convert the time entered in hh,min and sec into seconds.
hh = int (input('enter hrs'))
mm = int(input('enter miniute'))
ss = int(input('enter seconds'))

total = (hh * 3600) + (mm * 60)+ ss
print(f'total seconds is {total}')