# Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

li =["apple","oranges","mango","apple","mango","oranges","oranges"]

def occurance(li):
    unique_words =set(li)
    print(unique_words)
    for i in unique_words:
        count =0

        for word in li:
            if word ==i:  # word == unique word
                count +=1

        print(i,":",count)

occurance(li)
