tasks = ["plan", "code"]

tasks[0] = "design"
tasks.append("test")
tasks.insert(1, "review")
print(tasks)

#########

scores = [88, 72, 95, 81]

scores.remove(72)
last = scores.pop()
scores.sort()

print(scores)
print(last)

#####

students = ["mashail","omar","lina"]

for student in students:
    print(student)
for index, student in enumerate(students):
    print(index,student)

######

matrix = [
[1, 2, 3],
[4, 5, 6],
]
print(matrix[0])
print(matrix[1][2])

######

location = (24.7136, 46.6753)

print(location[0])
print(location[-1])

#location[0] = 25 # type error

########

student = ("mashail", 22, "python", 33, "kh", 77)

name, age, course, *others = student
print(name)
print(age)
print(course)
print(others)

#######

skills = {"python", "Git", "python"}

skills.add("Django")

print(skills)
print("Git" in skills)
print(len(skills))

#######

backend = {"python", "Django", "SQL"}
frontend = {"HTML", "CSS", "JavaScript", "SQL"}

print(backend | frontend) # يطبع الاثنين
print(backend & frontend) # يطبع الاشياء المشتركه
print(backend - frontend) # يطبع الاشياء اللي موجره بالاول مو موجوده بالثاني 
print(frontend - backend) # يطبع الاشياء اللي موجره بالاول مو موجوده بالثاني

########

student = {
    "name": "mashail",
    "age": 22,
    "course": "python"
}

print(student["name"])

#######

student = {"name": "mashail", "score": 90}

student["score"] = 95
student["grade"] = "A"

email = student.get("email", "not set")
grade = student.pop("grade")

#######

student = {"name": "mashail", "score": 90}
 
for key in student:
    print(key)
for key, value in student.items():
    print(key, value)

#######

names = [ "mashai", "Omar"]
skills = {"python", "Git"}
student = {"name": "mashail", "score": 95}

print(len(names))
print("python in skills")
print("name" in student) # checks keys

########

students = [
{"name": "mashail", "score": 95},
{"name": "omar", "score": 88}
 ]

for student in students:
 print(student["name"], student["score"])






