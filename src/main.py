def main():
    student_name = "mashail"
    student_age = "22"
    greetUser(student_name, student_age)


def greetUser(name, age):
    print(f"Welcome {name}, You are {age}")


main()

#Syntax_Practice
#Python_is_Case_Sensitive:
student_name = "Abdullah"
student_name = "Sara"
print(student_name)

#If_Statement_Syntax
score = 100
if score >= 80:
    print("Exellent!")
else:
    print("Thank you!")

#Data_Types:

student_name = "Nouf"
student_age = 20
course = "Web Development Bootcamp"
registred = True

MAX_CLASS_SIZE = 25
MIN_CLASS_SIZE = 15

print(f"""
Welcome {student_name} to {course}
You are {student_age}
Registration Status: {registred}

""")

#How_to_know_data_type
student_name, student_age, student_is_registred = "Nouf", 24, True
print(type(student_age))
print(type(student_name))
print(type(student_is_registred))
print(isinstance(student_age, str))

#Where to use (isinstance)?
#Case 1:
age = input("Enter your age:")
if (isinstance(age, int)):
    print("You are", age+5, "after 5 years")
else:
    print("You are", int(age)+5, "AFTER 5 years")
#Case 2:
age = int(input("Enter your age:"))
if (isinstance(age, int)):
    print("You are", age+5, "after 5 years")
else:
    print("You are", int(age)+5, "AFTER 5 years")

############################


teacher_name = "Faisal"
print(teacher_name)
index = int(input("Select an index:"))
if index < len(teacher_name):
    print(teacher_name[index])
else:
    print("Out of Range!")



