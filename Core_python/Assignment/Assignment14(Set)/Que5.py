# Write a Python program to find the longest common prefix of all
# strings. Use the Python set.

li =["flower","flight","flow","flipkart"]

def longest_common_prefix(li):
    li.sort()
    first = li[0]
    last = li[-1]
    ans =[]
   
    for i in range(min(len(first),len(last))):
        if(first[i] != last[i]):
            return ''.join(ans)

        ans.append(first[i])

    return ''.join(ans)


res =longest_common_prefix(li)
print(res)


# using set

# strings = ["flower", "flow", "flight"]

# def common_prefix(strings):
#     prefix = ""

#     for i in range(len(strings[0])):
#         s = set()

#         for word in strings:
#             if i < len(word):
#                 s.add(word[i])

#         if len(s) == 1:
#             prefix += strings[0][i]
#         else:
#             break

#     print(prefix)

# common_prefix(strings)
