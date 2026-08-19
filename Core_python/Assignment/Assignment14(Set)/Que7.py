# Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.


s1 ={1,2,3,4,5}
s2 ={3,4,5,6,7}
# with built in function (difference i.e a-b)
# def missing_ele(s1,s2):
#     missing_in_sec =s1 -s2
#     missing_in_first = s2 - s1

#     print(missing_in_sec)
#     print(missing_in_first)

# missing_ele(s1,s2)

# without built in function
def missing_ele(s1,s2):
    missing_in_first =set()
    missing_in_sec = set()

    for i in s1:
        if i not in s2:
            missing_in_sec.add(i)

    for i in s2:
        if i  not in s1:
            missing_in_first.add(i)

    print(missing_in_sec)
    print(missing_in_first)

missing_ele(s1,s2)
