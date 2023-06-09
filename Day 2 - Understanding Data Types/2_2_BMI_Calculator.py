# BMI Calculator that checks how overweight you are based on your weight & height
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_parsed = float(height)
weight_parsed = float(weight)

bmi = weight_parsed / (height_parsed ** 2)

print(f"Your BMI is: {int(bmi)}")
print("This means you are:")
print("Drumroll please...")
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal")
elif bmi > 24.9 and bmi <= 29.9:
    print("Overweight")
elif bmi > 29.9 and bmi <= 34.9:
    print("Obese")
elif bmi > 34.9:
    print("Extremely Obsese")
