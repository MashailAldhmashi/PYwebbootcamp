user_score = float(input("Enter your score: "))

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

grade = calculate_grade(user_score)
print(f"Grade: {grade}")






