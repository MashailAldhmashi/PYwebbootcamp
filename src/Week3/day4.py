numbers = [ 1, 2, 3, 4, 5] # اسمه expression يعني يعطيني قيمه

squares = [ #  اسمهexpression
 number ** 2 # اسمه compnention
 for number in numbers 
 if number % 2 == 1 
    ] # اسمه compnention

print(squares)  #[1, 9, 25] #  اسمه close 

##########
prices = [10, 25, 40]

prices_with_vat = [
    round(price * 1.15, 2)
    for price in prices
]

print(prices_with_vat)

##########

scores = [42, 67, 91, 58, 75]

passing_scores = [
    score
    for score in scores
    if score >= 60
]

print(passing_scores)

###########

raw_names = [" mashail ", "", "OMAR", " lina "]

clean_names = [
    name.strip().title()
    for name in raw_names
    if name.strip()
]

print(clean_names)

###########

numbers = [1, 2, 3, "c"] # Row
letters = ["A", "B"] # colum

pairs = [
    (number, letter)
    for number in numbers
    for letter in letters
]
print(pairs)

###########

scores = [ 42, 67, 91]

labels = [
    "pass" if score >= 60 else "retry"
    for score in scores
]

print(labels)

############

emails = [
    "mashail@EXAMPLE.COM",
    "foz@example.com",
    "farah@school.sa"
]

domains = {
    email.split("@")[1].lower()
    for email in emails
}

print(domains)

###########

numbers = range(1, 6)

squares = {
    number: number **2
    for number in numbers
}
print(squares)

############

