# name = input("Enter the name: ").strip()
# score_input = input("Enter score (0-100): ").strip()
# course = input("Enter select course: ").strip() 
# student_name = input("mashail,Foz")
# select_course = input ("python,asp.net, react")



# print("Validation ruselt")

# if not name :
#     print("Error: Name cannot be empty")

#     if score_input.isdigit() and int(score_input) >= 0 and int(score_input) <= 100:
#      score = int(score_input)
    
#     if score >= 90: 
#     print("A")
#     elif score >= 80: 
#     print("B")
#     elif score >= 70: 
#     print("c")
#     elif score >= 60: 
#     print("D")
#     else:
    
#     print("")


# age = 20
# if 18 <= age:
#    print("Welcome")
#    print("Code completed")

#Lap 4
is_active = True
is_verified = True
role = "editor"
is_blcoked = False

if is_active and is_verified:
    print("Account is ready")

if role ==  "admin" or role == "editor":
    print("User can edit")

if not is_blcoked:
    print("User is not blocked")
else:
    print("User is blocked")

#Lap 5
account_active = True
has_permission = False

if account_active:
 if has_permission:
    print ("Acces Granted")
 else:
    print("Acces denied")
else:
 print("Account is not active")

 #Lap 6
 name  = "mashai"
 cart = []
 balance = 0

 if name:
    print("name has a value")
    if not cart:
       print("your cart is empty, please shop")
       print(bool)(balance)

#LAp 7
name = input("please enter your name").strip()  

if not name:
   print("please enter a name")
elif not name.replace("","").isalpha():
   print("name must contain letters")
else:
   print(f"valid name{name}")

#Lap 8
age_text =input("Enter your age: ").strip()

if age_text.isdigit():
   age = int(age_text)
   print(f"You will be {age + 5} in 5 years")
else:
   print("Enter a number")

#Lap 9

score_text = input("Enter a number between 0 and 100")

if score_text.isdigit():
   score_x = int(score_text)

   if score_x >= 0 and score_x <=100:
      print("valid score")
      is_score_valid = True
   else:
      print("Score is invalid")
else:
 print("please enter a number")

 #Lap 10
 membership = ["admin","Editor","viewer"]

 current_membership = input("Enter ypur membership").strip().lower()
 if current_membership.title()in membership:
      print("you are allowed to view the content")
      print("current_membership")
 else:
    print("please contact admin team")
    print("current_membership")

#Lap 11

command = input("please enter a command (start, stop, status)").strip().lower()

match command:
      case "start":
       print(".....starting system")
      case "stop":
       print("stopping system")

      case "status":
       print("system is up and running ")

   


