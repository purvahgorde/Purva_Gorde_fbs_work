days = int(input('enter days '))

years = days // 365
print(years)

days =days % 365
print(days)

weeks =days //7
print(weeks)

days = days % 7 
print(days)

print(f'the year is {years} ,weeks is {weeks} and remaining days is {days}')