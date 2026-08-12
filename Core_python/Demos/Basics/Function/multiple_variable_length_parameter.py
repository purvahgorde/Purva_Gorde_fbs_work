# to pass multiple value with meaning in function
# menstion astrick(**) symbol before parameter name in function defination
# data stored in dictonary format
# use for loop on dict.items( to access individually

def emp(**data):
    for keys,value in data.items():
        print(keys,':',value) # it use acces individual value

    # for i in data:
    #     print(i) # it print only id

    # for i in data.items():
    #     print(i) # it gives output in tuple format

    

emp(id=101,name='Ninad',age =22,add='Pune')