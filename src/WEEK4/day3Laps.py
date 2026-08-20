class Dog:
  _legs = 4
  def __init__(self,name):
        self.name = name

  def getLegs(self):
            return Dog._legs # self مره استخدم السيلف مره الDog اشوف وش يطلع لي 
        
  def setLegs(self,number):
            self._legs = number

myDog = Dog("slugi")
myDog.setLegs(3)
print(myDog.getLegs())
print(myDog._legs)

#----------------------------------
#Lap1 
class Ticket:

    def __init__(self, name, status = "open"):
        self.name = name
        self.status = status

    def newStatus(self, status):
        self.status = status
myTicket1 = Ticket("1000","in progress")
myTicket2= Ticket("1001","pending")
print(myTicket1.status)
print(myTicket2.status)  # سوينا تيكتين 
#-----------------------------------
#Lap 2
class Greeter:
    def __init__(self, message):
      self.message = message
    def greet(self,user):
      self.user = user

      print(f"Hello {user}, {self.message}") # Return هينا يعطيني القيمه لو حطيت في الطباعه mymsg
mygreet = Greeter("Welcome To tuwiq")

mymsg = mygreet.greet("mesho")
# print(mymsg)
#------------------------------------
#Lap 3
class Welcome:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome{self.name}")

students = [
       Welcome("mashail"),
       Welcome("mesho"),
       Welcome("nouf"),
       Welcome("yamam")
]

for s in students:
    s.name = "Old student"
    s.welcome()
#---------------------------------
#Lap 4
from pathlib import Path

path = Path("home") / "students" / "students.txt"
path.parent.mkdir(parents=True, exist_ok=True)
# path.write_text("welcome to class", encoding="utf-8")
# print(path.is_dir())
# print(path.suffix)
# print(path.name)
# print(path.is_file())
#----------------------------------

#Lap5
#name-mangling
#property
class Student:

    _enrolled = True
    def __init__(self, name):
        self.name = name
        self.score = []

    def add_score(self, score):
        if 0 > score > 100:
            raise ValueError("score must be between 0 and 100")
        self.score.append(score)

        # Setter
    #@enrolled.setter
    def enrolled(self, status):
        self.__enrolled = status
        # Getter
    @property     
    def enrolled(self):
        return self.__enrolled
        

    @property   
    def average(self):
        if not self.score:
            return 0
        else:
            return sum(self.score) / len(self.score)
        
Student.enrolled = True
student = Student("khalifa")
student.add_score(80)
student.add_score(90)
student.add_score(100) 
print(student.average)
# student.setEnrollment(False)
# student._enrolled = True
# print(student.getEnrollment())
print(student.score)
#---------------------------------
#Lap 6 
class Food:
    def __init__(self, name):
        self.name = name
    def showName(self):
      return self.name
class Fruites(Food):
    newName = "MA"
    def __init__(self,cal,name):
     super().__init__(name)
     self.cal = cal

    @staticmethod
    def stripName(newName):
      return newName.strip()

myFruite = Fruites("Apple", 200)
print(myFruite.showName())
print(myFruite.stripName("MA"))
#---------------------------------
