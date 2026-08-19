# Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

li =[1,2,3,4,5,6,7,8,9]
target =9

def combination(li):
    res =set()
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            for k in range(j+1,len(li)):
                if(li[i] + li[j] + li[k] == target):
                    res.add((li[i],li[j],li[k]))

    print(res)

combination(li)


# o/p:- {(1, 2, 6), (2, 3, 4), (1, 3, 5)}