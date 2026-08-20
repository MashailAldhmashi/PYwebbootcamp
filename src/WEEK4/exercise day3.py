import json
from pathlib import Path

class StudentNotFoundError(Exception):
    pass

data_dir = Path("data")
data_dir.mkdir(exist_ok=True) 
file_path = data_dir / "students.json"

students = [
    {"name": "mashail", "score": 95},
    {"name": "Foaz", "score": 88},
]

with open(file_path, "w") as file:
    json.dump(students, file, indent=4)

try:
    with open(file_path, "r") as file:
        loaded_data = json.load(file)

    for student in loaded_data:
        if (
            "name" not in student
            or "score" not in student
            or not isinstance(student["name"], str) 
            or not isinstance(student["score"],  (int, float) ) 
        ):
            raise StudentNotFoundError(f" {student}")
    print("valadit")

except FileNotFoundError:
    print("error file not found.")
except json.JSONDecodeError:
    print("error json not found")

