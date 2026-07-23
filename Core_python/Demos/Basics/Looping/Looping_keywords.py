# 1 pass:-to neglect expected indentation error
for i in range(1,5):
    pass

# 2 break:- to terminate the loop
for i in range(1,10):
    if(i == 5):
        break;
    print(i)

# 3 continue:- to stop current iteration only
for i in range(1, 10):
    if(i == 5):
        continue
    print(i)

# 4 else:-will execute when loop is executed sucessfully
for i in range(1, 5):
    if( i == 6):
        break
    print(i)
else:
    print('for loop executed sucessfully')