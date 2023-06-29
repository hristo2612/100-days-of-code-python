# Fix the following code
"""
number = int(input("Which number do you want to check?"))

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
"""

# On line 5 the code does not check with == but instead uses assignment operator, here is the fixed code:
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
