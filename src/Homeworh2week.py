student_name = "Abdullah"
student_name = "Sara"
print(student_name)

score = 100
if score >= 80:
    print("Exellent!")
else:
    print("Thank you!")

student_name = "mashail"
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

student_name, student_age, student_is_registred = "mashail", 24, True
print(type(student_age))
print(type(student_name))
print(type(student_is_registred))
print(isinstance(student_age, str))