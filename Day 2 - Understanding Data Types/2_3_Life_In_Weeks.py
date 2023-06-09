# Calculating how many weeks/days/months you have left if you live to 90 years old
age = input("What is your current age? ")

current_age = int(age)
expected_age = 90

years_left = expected_age - current_age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(
    f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
