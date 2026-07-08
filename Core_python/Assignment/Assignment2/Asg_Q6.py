# WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

salary = int(input('enter basic salary '))

da = 10/100 *salary
ta = 12/100 *salary
hrs = 15/100 * salary

total_salary = salary + da +ta +hrs
print(f'total salary is {total_salary}')