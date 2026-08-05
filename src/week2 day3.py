#Lap 5

score = 10
score +=5
score = score + 5
score *+5

# print(f"Ypur score is {score}")

#Lap 6
membership =["Admin","Editor","Viewer"]
current_membership = "Editor"

if current_membership in membership:
    print("Welcome")
else:
     ("Go Home")

#Lap 7

stetence = "python web development"
# new_sentence = stetence.find("python")
if "python" in stetence:
    print("match found")
else:
    print("no match found")
      
# print(type(new_sentence))
# print(new_sentence)

#Lap 8

message = "Python Programming"
first_char = message[0]
last_char = message[-1]
print(f"First character is {first_char} and last character is {last_char}")
#slicing يفصل
sliced_message = message [:6]
print(sliced_message)
reveresed_message = message[::-1]
print(reveresed_message)
#reveresed يعكسها

#Lap 9
#strip يشيل المسافات 
my_email = "   mashail@eXample.com   "
cleaned_email = my_email.strip().lower()
message = "python web development"
titled_message = message.title()

print(f"Your emails is {cleaned_email}, and your course is {titled_message}")


#Lap 10

csv_text = "apple,orange,banana,cherry,dates"
splitted_text = csv_text.split(",")
print(splitted_text)
joined_text = " - ".join(splitted_text)
print(f"""ypur list is {csv_text}splitted like this {splitted_text}rejoined like this {joined_text}""")


#Lap 11 
name = "Khalid"
try:
    name[0] = "A"
except TypeError as e:
    print(e)

x = 5
y = 5
if (x == y):
    # i can try (x is y):
    #print("they are the same object")
    print("they are the same value")
else:
    print ("they are the same value")
#الid بعطيني رقم الميموري نمبر حقه الريفرنس 
print(id(x))
print(id(y))

#Lap 12
message = "python web development"
new_message = message.replace("development","Programing")
print(new_message)

#حل الواجب بتبديل القيم 
x = 5
y = 6
x,y = y,x
print(y)
print(x)

#####
is_online = None 

if(is_online == True):
    print("True")
elif(is_online == False):
    print("False")
else:
    print("None")



