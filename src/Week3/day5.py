numbers = range(1_000_000)

total = sum(
    number ** 2
    for number in numbers 
)

print(total) # lezy generate

##############

items = ["python","git"]
items.append("Django")

name = "mashail"
name = name.title()

print(items)
print(name)

###########
original = ["python","Git"]
alias = original

alias.append("Django")

print(original)
print(alias)
print(original is alias) #True

#############
original = ["python","Git"]
clone = original.copy()

clone.append("Django")

print(original)
print(clone)
print(original is alias) #False

###############
original = [["mashail", 90], ["omar", 85]]
clone = original.copy()

clone[0][0] = 95

print(original)
print(clone)
print(original [0] is clone[0]) #True

################
from copy import deepcopy
original = [["mashail", 90], ["omar", 85]]
clone = deepcopy(original)

clone [0][1] = 95

print(original)
print(clone)
print(original [0] is clone[0]) #True

##################
names = ["mashail","omar","lina"]

#searches otems one by one: o(n)
print("mashail" in names)

name_set = set(names)
#avarige membership
print("mashail" in name_set)

##################

