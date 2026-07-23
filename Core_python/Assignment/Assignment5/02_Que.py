# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.
nos = int(input('enter the no.of student:'))
count = nos
total_per =0
while(count>0):
    s1 = int(input('enter the marks subject 1:'))
    s2 = int(input('enter the marks subject 2:'))
    s3 = int(input('enter the marks subject 3:'))
    s4 = int(input('enter the marks subject 4:'))
    s5 = int(input('enter the marks subject 5:'))
    per = ((s1 + s2 + s3 + s4 + s5)/500)*100
    print(f'Percentage = {per}')

    total_per = total_per + per
    count -= 1
avg = total_per /nos
print(f'average percentage is {avg}')