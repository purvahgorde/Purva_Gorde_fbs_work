# To neglect the positional parameter
# Assign value to parameter in function call
# flow from right to left
# name of the parameter in the function call and function defination should be same 

def emp(id,name,salary,dept):
    data = 'Id:'+str(id)+"\n"
    data += 'Name:'+str(name)+'\n'
    data += 'Salary:'+str(salary)+'\n'
    data += 'Dept:'+str(dept)+'\n'
    return data

res = emp(name='john',id='101',dept='It',salary=20000) #change the oredr of positional parameter
print(res)