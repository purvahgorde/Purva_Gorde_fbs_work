# Write a Python program to remove the intersection of a second set
# with a first set.

# simple intersection remove kelya nanter je element rahatat te print karayche

# without built in function
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

for i in B:
    if i in A:
        A.remove(i)

print(A)

# wuth built in function
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.difference_update(B)

print(A)