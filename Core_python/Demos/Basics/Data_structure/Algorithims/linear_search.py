def linear_search(li,ele):
    for i in range(0,len(li)):
        if(li[i] == ele):
            return i
    else:
        return -1

ele = int(input('enter the number:'))
li =[20,38,54,76,90,87]
res = linear_search(li,ele)
if(res != -1):
    print(f' {ele} is found at postion {res}')
else:
    print(f'{ele} is not found')

    # time complexity is worste case O(n) ,best case O(1),average case O(n)
    # space complexity is O(1)