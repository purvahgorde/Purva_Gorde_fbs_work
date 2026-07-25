

for i in range(1, 6):

    # Print leading spaces
    for j in range(1, 7-i):
        print(" ", end=" ")

    # Print stars
    for j in range(1, i + 1):
        print("*", end="   ")

    print()