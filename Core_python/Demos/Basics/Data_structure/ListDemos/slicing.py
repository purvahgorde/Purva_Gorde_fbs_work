li =[10,20,30,40,50,60,70,80,90,100]

res =li[1:5:1] # li[start:end+1:gap]
res =li[5:9]
res =li[1:8:2]
res = li[:5] #starting 5 element
res = li[5:] # from 5 to last element
res = li[:] # complete list
res = li[: :] # complete list
res =li[4: :-1] # from 4 to one reverse
res =li[ :5:-1]
res =li[: :-1] #reverse list
res =li[ 5::-1]
print(res)