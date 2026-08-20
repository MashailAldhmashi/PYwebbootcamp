my_name = input("Enter your name: ")
print("hello", my_name)
#------------------
result = 6 == 3
print(result)
#------------------
result = 5 != 2
print(result)
#------------------
result = 3 > 2
print(result)
#------------------
result = 3 >= 3
print(result)
#------------------
result = 1 <= 3
print(result)
#------------------
not_foggy = True
not_raining = True
is_sunny = not_foggy and not_raining
print(is_sunny)

#---------------------
is_foggy = True
is_raining = False
not_sunny = is_foggy or is_raining
print(not_sunny)

#---------------------
is_student = True
print(not is_student)

#---------------------
first, second = True, False
and_result = first and second  # False AND
or_result = first or second  # True OR
not_result = not first  # False NOT
print(and_result)
print(or_result)
print(not_result)

#-----------------
name = "Khalid"
age = 18
is_student = True
driving_license = None
print(type(name))
print(type(age))
print(type(is_student))
print(type (driving_license))
print(driving_license)

#------------------
complex_number = 10j
print(complex_number)

#-------------------
name = "Ali"
age = 20
weight = 58.5

float_number = float(age)
print(float_number)

#------------------------
int_number = int(weight)
print(int_number)

#------------------------
string_value = str(age)
print(string_value)
#print(type(string_value))

#-------------------------
name = "mashail"
names = ["mashai","nouf","Ali", 1, 2.5, True] # list تاخذ كل انواع البيانات
print(names)
print(names[0]) #يطبع لي اول اسم 
#-------------------------
# اغير عنصر بال index
names = ["mashai","nouf","Ali", 1, 2.5, True] # list تاخذ كل انواع البيانات
names[0] = "mshmsh" 
print(names)
#------------------------
names = ["mesho","abdullah","foz","Az"]
names.append("hanan") #append يضيف لي علي نهاية الlist 
print(names)
#------------------------
names = ["mesho","abdullah","foz","Az"]
names.insert(3, "abdulaziz") #insert اضيف علي المصفوفه واحدد المكان اللي ينضاف فيه
print(names)
#------------------------
names = ["mesho","abdullah","hssah","foz","Az"]
names.remove("hssah") #remove يحذف لي من اللسته
print(names)
#------------------------
names = ["mesho","abdullah","hssah","foz","Az"]
names.clear() # clear يحذف لي اللسته بدون مدخلات 
print(names)
#------------------------
#Tuples
child_one = ("Ahmad", "Riyadh", "1-1-2021")
print(child_one) # tuple  القيم اللي احطها ثابته غير قابله للتغير
print(child_one[0])
print(type(child_one))
#------------------------
child_one = ("Ahmad", "Riyadh", "1-1-2021")
# child_one[0] = "hamed" # هذا المثال جربت اغير وطلع لي ايرور بالتيرمينال
print(child_one) #TypeError: 'tuple' object does not support item assignment
#-------------------------
child_one = 'Ahmad', 'Riyadh', '1-1-2021' # طريقه ثانيه لل tuple بدون اقواس
print(child_one)
#-----------------------
#Dictionary يكون اسم لمرجع اي شي يكون المفتاح لهاذي الاشياء
#child_one = 'Ahmad', 'Riyadh', '1-1-2021'
child_one = {"name": "ahmad", "birth_city": "Riyadh", "birth_date": "1-1-2021" }
print(type(child_one))
print(child_one)
#-----------------------
child_one = {"name": "mashail", "birth_city": "Riyadh", "birth_date": "1-1-2021" }
print(child_one["name"])
print(child_one.values()) # values يطبع لي القيم 
print(child_one.keys()) # keys يطبع لي كل الكيز
#-----------------------
child_one = {"name": "mashail", "birth_city": "Riyadh", "birth_date": "1-1-2021" }
del child_one ["birth_date"] # del تحذف لي اي كيز مع القيمه حقتها 
print(child_one)  
#------------------------
age = 19
if age >= 18:
     print("You are an adult") # use if / else
else:
     print("You are not an adult")
#-------------------------
Path = "ios"       #I use if / elif / else
if Path == "Web development":
  print("Java Script")
elif Path == "ios":
    print("swift")
elif Path == "android":  
    print("kotlin")
else:
    print("something else")
#---------------------------
i = 1         #I use while loop  
while i <= 5: # استخدمه اذا عندي شرط 
    print(i)
    i += 1     # لازم اكتب هذا الشرط لو تركت البرينت يطبع ال i بيكرر الواحد الي مالا نهايه
#------------------------
students = ["ahmad","mohammed","omar","khalid"]    # I use For loop
for s in students: # استخدمه للتكرار
    print(s)
#---------------------------------
for n in range(7):    # I use for in rang()
    print(n)    
#---------------------------------
for n in range(2,7):    # هينا احدد من وين ابيه يبدا
    print(n) 
#---------------------------------
for char in "mashail":
    print(char)
#---------------------------------
def greet():
   name = input("Please Enter Your Name: ")
   time = input("Please enter the time of the day: ")
   print( "Good "+time+"," +name+" !")       # Good Morinig,mashail!
greet() 
greet() # كذا استدعيها مرتين                 
#---------------------------------
def print_number():
    print(1)
    print(2)
    print(3)
    print(4)

print_number()
print_number()   #  اي تعديل على تعريف الداله فوق اللي هو بالfunction راح يظهر لي لما استدعي الداله
#---------------------------------
def print_number():
    for i in range(1,8):
      print(i) #
print_number() 
#--------------------------------
def print_number(to): # اي متغير اكتبه بين الاقواس مو شي ثابت الto
    for i in range(to):
      print(i) #هينا اذا مابي احط قيمه في الداله ابيها لما استدعيها لان الfunction وحده بس القيمه تختلف في الاستدعاء لكل مره
print_number(3) 
print_number(5) 
print_number(7) 
#---------------------------------
def add(first_number , second_number): #  هينا سويت الداله وحطيت فيها اكثر من باراميترز يعني مدخلين
    print(first_number + second_number) # هينا حطيت +
add(3,7) # هينا استدعيت الداله وحطيت لها قيمه
#--------------------------------
def add(first_number , second_number):  
    result = first_number + second_number     # نتيجه عمليه الجمع تخزنت في  result
    return result

value = add(1,6) 
value = add(1,2)
print(value)
#----------------------------------
def add(first_number , second_number):  
    result = first_number + second_number     
    return result

value = add(1,8) - add(3,2)   # هينا طرحت قيمتين 
print(value)
#------------------------------------
def add(first_number , second_number):  
    result = first_number + second_number     
    return result

value = add(1,8)     
print(value)
print_number(value) # هينا اخذت مخرجات داله وخليتها مدخلات لداله اخرى اللي هي print_number
#----------------------------------

def add(first_number , second_number):  
    return first_number + second_number 

print_number(add(1,8))     # هذا نفس الكود اللي قبله بس بشكل مختصر شلنا ال result وال add اضفناه داخل الداله
#-----------------------------------

