# Write a program to reverse a given number using recursive function.

# def reverse(num):
#     if(num >0):
#         digit = num % 10
#         print(digit,end='')
#         # return str(digit) + reverse(num // 10)
#         reverse(num // 10)
#     else:
#         return 0

# n =12345
# reverse(n)


def rev(num,sum=0):
    if num == 0:
        return sum 
    digit = num % 10
    sum =sum * 10 +digit
    return rev(num //10,sum)

n = 1234
res = rev(n)
print(res)
