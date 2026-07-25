#           * 
#         *   * 
#       *       * 
#     *           * 
#   *               * 
#   *               * 
#     *           * 
#       *       * 
#         *   * 
#           * 

#for upper
for i in range(1, 6):

    # Print leading spaces
    for j in range(1, 7-i):
        print(" ", end=" ")

    # Print stars
    for j in range(1, 2* i):
        if j == 1 or j == 2 * i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
#for lower 
for i in range(5,0,-1):
    for j in range(1,7-i):
        print(' ',end=' ')

    for j in range(1,2 * i):
        if j == 1 or j == 2 * i-1 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()