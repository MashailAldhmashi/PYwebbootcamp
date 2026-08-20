import csv

with open("students.csv", "w",  # csv صيغه مثل ال txt
          encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "course"])
    writer.writerow(["mashail", "python"])
    writer.writerow(["nouf", "django"])

#-------------------------------------
import json

students = [           # بدينا ليست بعدين مصفوفه
    {"name": "sara", "score": 92},
    {"name": "mashail", "score": 85}
]
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=2)

with open("students.json", "r", encoding="utf-8") as file:
        loaded = json.load(file)
print(loaded[1]["name"]) # loaded يحمل الملف # dump يكتب الملف 
#--------------------------------------
# try:
#   score = int(input("score: "))
# except ValueError:
#   print("Enter a whole number")
#   print("ValueError")

# print("program continues")
#---------------------------------------
from pathlib import Path

try:
    text = Path("students.txt").read_text(
    encoding="utf-8"
    )
except FileNotFoundError:
  print("student file not found")
except PermissionError:
  print("student file cannot be read")
#---------------------------------------
from pathlib import Path

path = Path("students.txt")

try:
    text = path.read_text(encoding="utf-8")
except OSError as error:
    print("load failed:', error")
else:
    print(text)
finally:
 print("load attempt finished")
 #--------------------------------------
 def validate_score(score):
    if not 0 <= score <= 100:
      raise ValueError("Score must be 0 to 100")
    return score

try:
    score = validate_score(120)
except ValueError as error:
    print(error)
#--------------------------------------
class StudentNotFoundError(Exception):
    pass
def find_student(name, students):
    for student in students:
        if student["name"] == name:
            return student
    raise StudentNotFoundError(name)

students = [{"name": "mashail"}]

try:
    print(find_student("ali", students))
except StudentNotFoundError as error:
    print("missing student:", error)
#--------------------------------------
