# Tip Calculator that receives the total bill, number of people and the tip percentage.
# It returns the total amount each person should give for the bill
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input(
    "What percentage tip would you like to give? 10%, 12% or 15%? "))
people = int(input("How many people to split the bill? "))

each_person_to_pay = (
    total_bill + (total_bill * (tip_percentage / 100))) / people
each_person_to_pay = round(each_person_to_pay, 2)

print(f"Each person should pay: ${each_person_to_pay}")
