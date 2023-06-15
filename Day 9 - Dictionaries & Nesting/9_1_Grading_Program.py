# Create a new dictionary for grades & calculate grades based on scores
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for name in student_scores:
    score = student_scores[name]
    if score >= 91 and score <= 100:
        student_grades[name] = "Outstanding"
    elif score >= 81 and score <= 90:
        student_grades[name] = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

print(student_grades)
