#           1 
#         2 3 2 
#       3 4 5 4 3 
#     4 5 6 7 6 5 4 
#   5 6 7 8 9 8 7 6 5 

for i in range(1,6):
    for j in range(1,7-i):
        print(' ',end=' ')
    k=i
    for j in range(1,i+1):
        print(k,end=' ')
        k += 1
    
    for j in range(i*2-2,i-1,-1):
        print(j,end=' ')
    print()