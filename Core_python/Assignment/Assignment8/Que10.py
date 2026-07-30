# Write a program to check if entered year is a leap year or not.
def leapYear(year):
    if((year % 400 ==0) or ( year % 4 ==0 and year % 100 !=0) ):
        print(f'{year} is leap year')
    else:
        print(f'{year} is not leap year')
year = int(input('enter a year:'))
leapYear(year)