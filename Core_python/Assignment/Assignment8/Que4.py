# Sum of all odd numbers between 1 to n
def oddSum(n):
    sum=0
    i =1
    while(i<=n):
        if(i % 2 !=0):
            sum = sum + i
        i +=1
    return sum

result =oddSum(5)
print('the odd sum is:',result)