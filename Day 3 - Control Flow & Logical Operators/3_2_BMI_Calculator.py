# BMI Calculator 2.0 - Incorporating if statements ( not that i didn't do it in the last calculator.. )
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height ** 2)
rounded_bmi = round(bmi)
template = f"Your BMI is {rounded_bmi}, you"

if bmi < 18.5:
    print(f"{template} are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"{template} have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"{template} are slightly overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"{template} are obese.")
elif bmi >= 35:
    print(f"{template} are clinically obese.")
