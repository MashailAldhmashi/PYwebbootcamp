from pathlib import Path
data_file = Path("data") / "students.txt"

print(data_file)
print(data_file.name)
print(data_file.suffix)
#------------------------
from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

data_file = data_dir / "students.txt" # انشئ لي الفولدر والملف 

print(data_dir.is_dir()) # هينا اتاكد اذا الفولدر موجود
print(data_file.exists()) # هينا اتاكد من الملف موجود
#-----------------------
# "r" red an existing file
# "w" write and replace content
# "a" append aftervexisting content
# "x" create only when absent

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("New not\n")
#------------------------
from pathlib import Path

path = Path("notes.txt")

with path.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)
print(file.closed) # True
#-------------------------
from pathlib import Path

path = Path("notes.txt")

with path.open("r", encoding="utf-8") as file:
    text = file.read()

same_text = path.read_text(encoding="utf-8")
print(text == same_text)
#-------------------------
# from pathlib import Path

# path = Path("students.txt")

# with path.open("r", encoding="utf-8") as file:
#    for line in file:
#      name = line.strip()
#      if name:
#        print(name) 
#-------------------------
from pathlib import Path
path = Path("students.txt")

with path.open("w", encoding="utf-8") as file:
   count = file.write("Sara\nAli\n")

print(count)
#-------------------------
from pathlib import Path

path = Path("activity.log") # لما انشئ الملف المفروض من التيرمنال ادخل cd بمكان المجلد اللي ابي اضيف ال file فيه 

with path.open("a", encoding="utf-8") as file:
    file.write("Student enrolled: Mashail\n") # لو شلت ال \n بيصير بالملف الطباعه جنب بعض ملف شذفهدهفغ.مخل

print("Activity saved")
#--------------------------
from pathlib import Path

names = ["Mashail", "Nouf","ymam"]
text = "\n".join(names) + "\n" # join تجمع لي الكلام على سطر واحد 

Path("students.txt").write_text(
    text,
    encoding="utf-8" # بالملف students يطبع لي الاسماء اللي اضفتها
)
#-------------------------