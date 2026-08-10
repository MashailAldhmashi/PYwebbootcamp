#Lap 1
def greet():
    print("welcome To python")
    
greet()

#Lap 2
def show_menu():
    print("1-coffee")
    print("2-tea")
    print("3-ginger")

show_menu
print("Outside the call")
show_menu()

#Lap 3
print("Lin one")
def gotofunc():
    print("from within the Goto")

print("where is line 2")
gotofunc()
print("Iam up here")

#Lap 4
def greet_student(name):
    print(f"Welcome {name}")
greet_student("mashai")
greet_student("frah")


#Lap 5
def show_booking(destination = "Riyadh", nights = 1):
    print(f"you'r traveling to {destination}, and will stay for {nights} nights")
show_booking("Riyadh")
show_booking("Doha", 2)

#Lap 6
def getVAT(total, rate = 0.15):
#"""this function will get the total with VAT added to it, and return the sum"""
    subtotal = total + (total * rate)
    return subtotal

print(getVAT(154))
print(getVAT(154, 0.05))
print(getVAT.__doc__)
#help(getVAT)

total =getVAT(680)
print(total)


