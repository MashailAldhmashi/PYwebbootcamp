# student = ["mashail","omar"]

import copy

students = [
    {"name": "mashail", "scores": [80, 90, 70]},
    {"name": "Omar", "scores": [60, 70, 80]},
    {"name": "Ali", "scores": [50, 40, 30]}
]

report = [{"name": s["name"], "scores": s["scores"], 
           "avg": sum(s["scores"])/len(s["scores"])} for s in students]

filtered = [s for s in report if s["avg"] >= 60]

student = {s["name"]: s for s in filtered}

backup = copy.deepcopy(student)

student["mashail"]["scores"][0] = 100

original = [["mashail", 90], ["omar", 85]]


# original = [["mashail", 90], ["omar", 80]]
clone = original.copy()

clone[0][0] = 90

print(original)
print(clone)
print(original [0] is clone[0])

print(student["mashail"]["scores"])  
print(backup["Omar"]["scores"]) 
print(student)

