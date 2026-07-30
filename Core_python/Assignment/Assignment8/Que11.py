# WAP to check if a given number is Armstrong number or not. For each task create separate functions.

def count(num):
    # count =0
    # i =1
    # while(num > 0):
    #     count += 1
    #     num = num //10
    # return count 

    length =len(str(num))
    return length


# result =count(1234)
# print(result)

def armstrong(num):
    sum = 0
    temp = num
    length = count(num)
    while(num >0):
        digit = num % 10
        sum = sum +(digit ** length)
        num = num //10

    if(temp == sum):
        print('Armstrong number')
    else:
        print('not Armstrong number')

num = int(input('enter a number:'))
armstrong(num)