# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
amount = int(input('enter amount '))

two_thousand = amount //2000
amount = amount % 2000
# print(two_thousand)

five_hundered = amount //500
amount = amount % 500
# print(five_hundered)

two_hundered = amount //200
amount = amount % 200
# print(two_hundered)

one_hundered = amount //100
amount = amount % 100
# print(one_hundered)

fifty_rs = amount //50
amount = amount % 50
# print(fifty_rs)

twenty_rs = amount//20
amount = amount % 20
# print(twenty_rs)

ten_rs = amount //10
amount = amount % 10
# print(ten_rs)

total = two_thousand +five_hundered + two_hundered +one_hundered + fifty_rs + twenty_rs + ten_rs

print(total)