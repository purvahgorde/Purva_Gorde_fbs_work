# Write a Python program to find elements in a given set that are not in
# another set.

s1 ={1,2,3,4,5}
s2 ={3,4,5,6}

# method1
# res = s1.difference(s2)
# print(res)


# method2
# res = s1 - s2
# print(res)


# method 3 using(set)
res =set()
for i in s1:
    if i not in s2:
        res.add(i)

print(res)