class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(f": {student.name}")
            print(f": {student.scores}")
            print(f": {student.average():.2f}")
            print("-" * 20)

student1 = Student("mashail")
student1.add_score(85)
student1.add_score(90)

student2 = Student("Sara")
student2.add_score(95)
student2.add_score(150) 

student3 = Student("Khalid") 

course = Course("Python")
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

course.display_students()
