def reverseNum(n):
    if(n >0):
        digit = n%10
        print(digit,end='')
        reverseNum(n // 10)

reverseNum(1234)
        