# def num(n):
#     if(n>5):
#         return
#     print(n,end=" ")
#     num(n +1)

# num(1)

# def num(start,end):
#     if(start >end):
#         return
#     print(start,end =' ')
#     num(start+1,end)

# num(3,7)

# def num(start,end):
#     if(start >end):
#         return
#     print(end,end =" ")
#     num(start,end -1)

# num(3,7)


# def num(n):
#     if(n<1):
#         return
#     print(n,end =' ')
#     num(n-1)

# num(5) 

# def even(n,N):
#     if n>N:
#         return
#     if(n % 2 ==0):
#         print(n,end =" ")
#     even(n + 1,N)

# N = int(input('enter the value of N'))
# even(1,N)  

# def even(n,N):
#     if n>N:
#         return
#     if(n % 2 !=0):
#         print(n,end =" ")
#     even(n + 1,N)

# N = int(input('enter the value of N'))
# even(1,N) 

def sum(start,N):
    
    if start >N:
        return 0
    
    return start +sum(start +1,N)
    

res =sum(1,5)
print(res)