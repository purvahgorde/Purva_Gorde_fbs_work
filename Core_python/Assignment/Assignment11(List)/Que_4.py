# 4. Python Program to Find the Second Largest Number in a List Using Bubble
# Sort

def bubbleSort(li):
    n =len(li)
    for i in range(0,n):
        for j in range(n - i -1):
            if(li[j] > li[j+1]):
                li[j],li[j+1] =li[j+1],li[j]


li =[40,15,78,90,43,19]
bubbleSort(li)
print(li)
print(f'second_largest no {li[-2]}')