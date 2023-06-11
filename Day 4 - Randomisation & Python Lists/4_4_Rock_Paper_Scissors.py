# Play rock paper scissors against computer.
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

possibilities = [rock, paper, scissors]

decision = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors... "))

if decision == 0:
    print(rock)
elif decision == 1:
    print(paper)
elif decision == 2:
    print(scissors)

print("Computer chose:")
computer_decision = random.randint(0, 2)
print(possibilities[computer_decision])

if computer_decision == decision:
    print("It's a draw")
elif computer_decision == 0 and decision == 1:
    print("You win")
elif computer_decision == 0 and decision == 2:
    print("You lose")
elif computer_decision == 1 and decision == 0:
    print("You lose")
elif computer_decision == 1 and decision == 2:
    print("You win")
elif computer_decision == 2 and decision == 1:
    print("You lose")
elif computer_decision == 2 and decision == 0:
    print("You win")
