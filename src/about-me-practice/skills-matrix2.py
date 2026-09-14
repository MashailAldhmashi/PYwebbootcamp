number = -999
print(abs(number))  #abs
#___________________
number = 3.699
print(round(number, 2))   #round
#___________________
number = 3
print(pow(number, 2))  #pow
# i can use this track
#--------
print(pow(3, 2))   #pow يكون اثنين اس ثلاثه
#-------------------
numbers = 300, 600, 900, 369, 786, 1093
print(max(numbers))     # max
numbers = 300, 600, 900, 369, 786, 1093
print(min(numbers))     #min
###
print(min(300, 600, 900, 369, 786, 1093)) # ican use this trak also in the min and max 
#______________________
numbers = 300, 600, 900, 369, 786, 1093
print(sum(numbers))
#______________________
import math
number = 144
print(math.sqrt(number))
#_______________________
import math
print(math.remainder(9, 3))
#______________________
import datetime
now = datetime.datetime.today()
print(now.day) # ican use month and year and today and hour and minute and second
#____________________
import datetime
date = datetime.date(2026,9,11)
time = datetime.time(3,6,9)
print(date)
print(time)
print (date.strftime('%A %B %Y)')) # if use %a the output Fri if use %A the out put Friday ican use %B / %b / %m for month like this
#   the out put ( Friday September 2026 )   
print(time.strftime('%I %M %S')) 
#________________________
alphabet = 'mashailaydehaldhmashi'
the_list = [3,6,9]
the_tuple = (3,6,9,9)
print(alphabet[6])  #if i want start from first use it 0 if i want start from the end i can use -1     
print(alphabet[-1]) 
print(the_list) # list
print(the_tuple) #tuple
#________________________
# Slicing #
text = 'this is Python course'
print(text[8:14])     # احدد من وين يبدا يطبع لي الindex ووين ينتهي ال out put  Python
print(text[7:])   # اذا حددت البدايه بيبدا يطبع منها الى اخر شي  output ( Python course )
print(text[:7]) # هينا بيبدا من البدايه وبيوقف عند اللي حددته 7 output ( this is )
#______________________
the_string = 'this is the student nora'
the_list = [1,2,2,3,3,3,3]
the_tuple = (4,4,4,4,5,5,5,5,5)
print(the_string.count('s')) #  يطلع لي كم مره تكرر الحرف اوالكلمهthe out put 3
print(the_list.count(2)) # the out put 2
print(the_tuple.count(5)) # the out put 5
#_________________________

