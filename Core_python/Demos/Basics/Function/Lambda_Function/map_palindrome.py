def chkPalindrome(num):
    temp = num
    rev =0
    while(num >0):
        d = num % 10
        rev = rev * 10 +d
        num = num //10

    if(temp == rev):
        return True
    else:
        return False

data =[122,121,123321,154]

res = list(map(chkPalindrome,data))
print(res)


