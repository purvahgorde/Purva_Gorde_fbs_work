# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
nop = int(input('enter the nop:'))
count = nop
total_amt =0
while(count >0):
    tic =int(input(f'enter the cost per person tickect : '))
    age = int(input('enter age of the person:'))
   
    if(age <12):
        total_amt =total_amt +(tic -(tic* 0.3))
    elif(age>59):
        total_amt = total_amt +(tic -(tic* 0.5))
    else:
        total_amt = total_amt + tic
    count -= 1
print(total_amt)

