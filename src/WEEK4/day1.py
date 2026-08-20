class Student:
    def __init__(self, name, score):
     self.name = name
     self.score = score

student = Student("mashail", 92)

print(student.name)
print(student.score)

#------------------
class Student:
    def __init__(self, name):
     self.name = name
    def introduce(self):
     print(f"I am Omar{self.name}")

student = Student("Omar")
student.introduce()
#-----------------------
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

sara = Student("sara", 92)
omar = Student("omar", 81)

sara.score = 95

print(sara.score)
print(omar is isinstance)
#-------------------------
class Student:
    academy = "Tuwaiq Academy"

    def __init__(self, name):
        self.name = name

sara = Student("Sara")

print(Student.academy)
print(sara.academy)
#------------------------
class Student:
    def __init__(self, name, score):
      self.name = name
      self.score = score

    def display_result(self):
         print(self.name , self.score)

student = Student("lina", 88)
student.display_result()
#----------------------
class Counter:
   def __init__(self):
       self.value = 0
   def increment(self):
       self.value +=1

counter = Counter()
counter.increment()
counter.increment() 

print(counter.value) #2
#----------------------
class Rectangle:
    def __init__(self, width, height):
      self.width = width
      self.height = height

    def area(self):
        return self.width * self.height
      
rectangle = Rectangle(5,3)
print(rectangle.area())  
#--------------------------
class BankAccount:
   def __init__(self,balance=0):
      self.balance = balance

   def withdraw(self, amount):
     if amount <= 0 or amount > self.balance:
       return False
     self.balance -= amount
     return True
      
account = BankAccount(500)
print(account.balance)
print(account.withdraw(200))
print(account.balance)

#---------------------
class Student:
   def __init__(self, name, score):
      self.name = name
      self.score = score 
   def __str__(self):
      return f"{self.name}: {self.score}"
      

#----------------------
class Counter:
    def __init__(self):
      self.value = 0
    def increment(self):
     self.value += 1
first = Counter()
second = Counter()

first.increment()
print(first.value)
print(second.value)
#-----------------------
class Student:
   def __init__(self, name):
      self.name = name
   def greet(self):
      return f"Hello,{self.name}"
      
students = [
         Student("sara"),
         Student("omar"),
         Student("lina")
      ]

for student in students:
         print(students[0].greet()) # لو حطيت بدال ال 0 رقم واحد بيطلع لي ثاني اسم اللي هو omar
#-----------------------
class Student:
   pass

student = Student()

print(type(student))
print(type(student) is Student)
print(isinstance(student, Student))
#------------------------
class Student:
   def __init__(self, name, score):
      self.name = name
      self._score = score
student = Student("Mashail", 93)
student = Student("KH", 99)

print(student.name)
print(student._score) # هاذي العلامه يعني غير قابل للتعديل .ـ #accessible, 
# but treated as internal

#------------------------
class Student:
   def __init__(self, name, scores):
    self.name = name
    self.scores = scores

   def average(self):
      return sum(self.scores) / len(self.scores)

   def add_score(self, score):
      if 0 <= score <= 100:
       self.scores.append(score)

student = Student("mashail",[80, 90])
student.add_score(100)
print(student.name, student.average())
#----------------------