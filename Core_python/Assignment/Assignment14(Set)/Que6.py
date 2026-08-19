# Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.

li =[2,3,4,5,7]

def product(li):
    pairs =set()
    max_prod =0
    res =()

    for i in range(len(li)):
        for j in range(i+1,len(li)):
            pairs.add((li[i],li[j]))  # it gives all possible pairs

    for a,b in pairs:
        prod =a *b 
        if(prod > max_prod):
            max_prod = prod
            res =(a,b)

    print(res)
    print(max_prod)       

product(li)


# without using set
# li = [2, 5, 3, 9, 1]

# def max_product(li):
#     max_product = 0
#     result = ()

#     for i in range(len(li)):
#         for j in range(i + 1, len(li)):
#             product = li[i] * li[j]

#             if product > max_product:
#                 max_product = product
#                 result = (li[i], li[j])

#     print(result)
#     print(max_product)

# max_product(li)