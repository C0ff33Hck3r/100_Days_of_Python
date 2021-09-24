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


question1 = input("Welcome to Treasure Island. Which direction would you like to go? Left or Right?\n")

question2 = input("You arrive at a river where the water is moving rapidly. You hear a hissing noise in the distance. It could be a viscious snake. \nShould you wait out the dangerous waters, or take the risk and swim across? Wait or Swim?\n")

question3 = input("You stumble upon 3 mysterious doors inside of the jungle. Which door do you choose? Red, Blue, or Yellow?\n")


if question1 == "Left":
  if question2 == "Wait":
    if question3 == "Yellow":
      print("Congratulation!!! You have found the islands treasure!")
    elif question3 == "Red":
      print("You were so close! You will now be burned by the fire. Game Over")
    elif question3 == "Blue":
      print("There was a bear on the other side of this door. Now he get's lunch! Game Over")
    else:
      print("That was not an option. Game Over")
  else:
    print("You should have waited. Those waters were too dangerous.")
else:
  print("That was fast! Try again next time")


