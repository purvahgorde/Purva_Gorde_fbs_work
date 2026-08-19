# Python Program to Concatenate Two Dictionaries Into One
student1 ={"rollno":1,
          "name":"john",
          "class":10,
          }

student2 ={"section":"A",
           "city":"pune"
           }
# with built in function
def student(stu1,stu2):
    stu1.update(stu2)
    print(stu1)

student(student1,student2)


# without built in function
def student(stu1, stu2):
    for key in stu2:
        stu1[key] = stu2[key]

    print(stu1)

# dictionary["new_key"] = value
# If the key doesn't exist → create it.
# If the key already exists → update its value.