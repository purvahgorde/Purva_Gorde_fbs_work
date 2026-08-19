# Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

li =[1,2,3,4,5]
target = 5

def sum(li):
    res=set()
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if(li[i] + li[j] == target):
                res.add((li[i],li[j]))

    print(res)

sum(li) 



# using set
# li = [2, 4, 3, 5, 7, 8, 9]
# target = 10

# def find_pairs(li, target):
#     seen = set()

#     for num in li:
#         complement = target - num

#         if complement in seen:
#             print(complement, num)

#         seen.add(num)

# find_pairs(li, target)