print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
decisionOne = input(
    "You are at a crossroad, you can go left or right. Which way you want to go? 'left' or 'right'\n")

if decisionOne == "left":
    decisionTwo = input(
        "You arrive at a river, do you decide to 'swim' or 'wait'?\n")
    if decisionTwo == "wait":
        decisionThree = input(
            "You wait for the boat to pick you up. It takes you to the other side.\nYou continue to walk and you see a big house.\nThere are 3 doors to choose. Which one do you choose? 'blue', 'red' or 'yellow'\n")
        if decisionThree == "yellow":
            print("YOU FOUND THE TREASURE!")
        else:
            print("Game Over.\nYou opened the door and there was a serial killer behind it. He told you that you should have picked the other door and then killed you like a dog.")
    else:
        print("Game Over.\nYou were too impatient and decided to swim accross this big ass river. Now you drowned..")
else:
    print("Game Over.\nTaking the 'right' path leads you to a gang of thugs and they rob you and kill you.")
