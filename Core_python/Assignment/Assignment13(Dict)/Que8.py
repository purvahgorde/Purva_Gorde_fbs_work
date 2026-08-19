# Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary

str1 = "apple mango orange grapes mango orange"

def frequency(str1):
    di = {}

    for word in str1.split():
        if word in di:
            di[word] += 1
        else:
            di[word] = 1

    print(di)

frequency(str1)