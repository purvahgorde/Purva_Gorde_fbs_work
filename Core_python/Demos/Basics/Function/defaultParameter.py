# Default parameter is use for 
# 1.to make parameter optional(why)
# 2.Assign a value to default parameter in function defination (how)
# 3.If we pass the value to parameter it take it otherwise it take default value(what)
# 4.flow is right to left


def emp(id,name,sal=20000,dept='IT'):  # if all variable has default value then there is no error otherwise it give error positional parameter
    print('Id:',id)
    print('Name:',name)
    print('salary:',sal)
    print('Dept:',dept)

emp(101,'john',50000,'DA')
print('###########################')
emp(100,'lina')
print('############################')
emp(102,'Deo')
