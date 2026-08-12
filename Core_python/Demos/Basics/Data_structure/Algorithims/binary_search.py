# Requirement 
# 1. Duplicate element are not allowe
# 2. sorted list (ascending order)

def binarySearch(li,ele):
    low =0
    high = len(li) -1

    while(low <= high):
        mid =(low +high) //2
        if(ele == li[mid]):
            return mid
        elif(ele > li[mid]):
            low =mid +1
        elif(ele <li[mid]):
            high = mid -1
    else:
        return -1

li =[10,20,30,40,50,60]
search_ele =int(input('enter the elemnt:'))
res = binarySearch(li,search_ele)

if(res != -1):
    print(f'{search_ele} element is present at index {res}')
else:
    print('element is not present')