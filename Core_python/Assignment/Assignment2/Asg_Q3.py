# Convert distant given in feet and inches into meter and centimeter.
feet = int(input('enter distance in feet '))
inches = int(input('enter distance in inches '))

total_inches = (feet * 12) + inches # convert feet to inches

total_cm = total_inches *2.54  # conver into cm

meters = int(total_cm//100)
cm =total_cm % 100

print(f'distance in meters is {meters} and centimeter is {cm}')