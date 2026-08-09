# Write a program to find the second largest element in the list.
li =[20,39,54,45,67,89,35]

largest =li[0]
sec_largest = li[0]

for i in range(0,len(li)):
    if(li[i] > largest):
        sec_largest = largest
        largest = li[i]

    elif(li[i] >sec_largest and li[i] != largest):
        sec_largest = li[i]

print(f'the second largest element is {sec_largest}')