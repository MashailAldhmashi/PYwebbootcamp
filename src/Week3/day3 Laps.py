#Lap 1
students = ["mashail", "dalal", "taif","frah"]

for studnet in students:
    print(studnet)

for iterable in enumerate(students):
    print(iterable)

#Lap 2
set_col = {"abdullah", "nasser", "dalal","mshmsh"}
tuple_col = (11,22,33,44,55,66)
dict_col = {"name":"abdullah", "age":22,}
list_col = ["ABC", 333,(33,33)]

# for c in dict_col.value():
# print(type(c))

print(set_col)
print(tuple_col)
print(dict_col)
print(list_col)

print(type(set_col))
print(type(tuple_col))
print(type(dict_col))
print(type(list_col))

#lap 3
cars = ["GMC", "BMW", "Geely", "porsche","merc","chevy"] # type cars

print(cars[3])
print(cars[-1])
print(cars[-1::-1])

#Lap 4
# the nivigation
tasks = ["Read email", "open ticket"]

tasks[0] = "login"
tasks.append("Get coffee")
tasks.insert(0, "Get breakfast")
tasks.pop(3)
print(tasks)

#Lap 5
nums = [ 11,22,33,44,55,66]

print(sum(nums))
print(len(nums))
print(max(nums))
print(min(nums))
print(nums)
print(nums.pop(2))
print(sorted(nums, reverse=True))

#Lap 6
skills = {"python", "Django", "flask", "fastAPI", "Java"}
skills.add("CSS")
skills.add("HTML")
skills.remove("Java") # هذا الامر يحذفها
skills.discard("Java") #  هذا الامر يتجاهل 
print(skills)

