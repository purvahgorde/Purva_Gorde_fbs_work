# Sum of all prime numbers between 1 to n
def primeNumber(start,end):
    sum =0
    for num in range(1,end+1):
        if( num>1):
            for i in range(2,num):
                if(num % i ==0):
                    break;
            else:
                print(num,end=' ')
                sum =sum +num
        else:
            print('enter valid number')
    print('sum of all primne number betwn 1 to n is:',sum)

end = int(input('enter a end number:'))
primeNumber(1,end)