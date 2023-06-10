# A dumb love calculator that checks how many times the words "TRUE LOVE" occur in both of you & your partners names
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = f"{name1}{name2}".lower()

trueCount = 0
loveCount = 0

trueCount += combined_names.count('t')
trueCount += combined_names.count('r')
trueCount += combined_names.count('u')
trueCount += combined_names.count('e')

loveCount += combined_names.count('l')
loveCount += combined_names.count('o')
loveCount += combined_names.count('v')
loveCount += combined_names.count('e')

compatibility_percent = int(f"{trueCount}{loveCount}")

if compatibility_percent < 10 or compatibility_percent > 90:
    print(
        f"Your score is {compatibility_percent}, you go together like coke and mentos.")
elif compatibility_percent >= 40 and compatibility_percent <= 50:
    print(f"Your score is {compatibility_percent}, you are alright together.")
else:
    print(f"Your score is {compatibility_percent}.")
