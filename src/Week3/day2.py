#Lap 1
course = " Web Development Bootcamp"
duration = 12

def type(course):
    print("Opss!")

print(course)
print(duration)
print(type(course))

#Lap 2
building = "Tuwaiq"
cohort_size = 20

print(f"Welcome To {building}, class limit is {cohort_size}")
print("Tuwaiq" in building)
print("cohort_size" in globals())
print(globals()["building"])

#Lap 3
loction = "Outter"
def outter():
 print(f"From {loction}")
def inner():
        loction = "Outter"
        print(f"From {loction}")
        inner()
outter()

#Lap 4
loction = 1
def outter():
 print(f"From {loction}")
def inner():
        loction +=2
        print(f"From {loction}")
        inner()
outter()

#Lap 5
#هذا المثال عشان افهم الfunction وكيف استدعي وحده داخل وحده 

def printer():
    print("Welcome")

def desk():
    printer()

def room():
    desk()

def house():
    room()

def city():
    house()

def country():
    city()

country()

#Lap 6
language = "python"
def  show_lang(language):
    print(language)
    show_lang("Dart")
    print(language)

#lap 7
rate = 0.15
def getTotal(amount):
    total = amount * rate + amount
    return total
print(f"{getTotal(199.99):.2f}")
print(round(getTotal(199.99),2))

#Lap 8
def inspect_order(item, qty):
    subtotal = 25 * qty
    print(locals())
    print(locals()["subtotal"])
inspect_order("Pen", 10)
               
           
