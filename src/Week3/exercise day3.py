
students = [
    {
        "name": "mashail",
        "scores": (85, 90, 95),
        "skills": {"Python", "SQL"}
    },
    {
        "name": "foz",
        "scores": (70, 80, 75),
        "skills": {"HTML", "CSS"}
    }
]

for student in students:
    student["skills"].add("Git")
    
    total_score = 0
    for score in student["scores"]:
        total_score += score
    average = total_score / len(student["scores"])
    
    print(f"Name: {student['name']}")
    print(f"Average: {average:.2f}")
    print(f"Skills: {student['skills']}")
    print("-" * 25)
