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

#Python code below this line

StepChoice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n')
StepChoice1 = StepChoice1.lower()
if StepChoice1 == "left":
   StepChoice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n')
   StepChoice2 = StepChoice2.lower()
   if StepChoice2 == "wait":
      StepChoice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")
      StepChoice3 = StepChoice3.lower()
      if StepChoice3 == "red":
         print("It's a room full of fire. Game Over.")
      elif StepChoice3 == "yellow":
        print("Congratulations, you found the treasure! You Won!")
      elif StepChoice3 == "blue":
        print("You encountered beasts in the room. Game Over.")
      else:
         print("You chose a door that doesn't exist. Game Over!")
   else:
    print("You got attacked by an angry trout. Game Over!")
else:
  print("You fell into a hole. Game Over!")