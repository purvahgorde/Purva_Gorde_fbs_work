# Write a program to check whether a number is prime or not using recursion.
def prime(num , i): #(25,12)
    if num<=1:
         return False
    elif i == 1:
         return True
    elif(num % i==0):
        return False
    return prime(num ,i-1) #(25 ,11) and so on till condition false i.e (25,5)
        
          

def is_prime(num): #num =25
    if(prime(num, num//2)): # (25,12)
        print(f'{num} is prime number')
    else:
        print(f'{num} is not prime number')
    
n=25
is_prime(n)