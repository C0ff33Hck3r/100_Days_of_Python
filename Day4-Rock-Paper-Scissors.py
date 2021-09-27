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

import random


print("Welcome to my Rock, Paper, Scissors game!")

user_choice = int(input("What will you choose...\nType 0 for Rock, 1 for Paper, and 2 for Scissors."))

generator = [rock, paper, scissors]

#User choice
print("You chose: ")
print(generator[user_choice])


#Computer choice
computer_choice = random.randint(0,2)
print("Computer chose: ")
print(generator[computer_choice])

if user_choice >= 3 or computer_choice < 0:
  print("That input is invalid. Try again.")
elif user_choice == 0 and computer_choice == 2:
  print("Nice One!")
elif user_choice == 1 and computer_choice == 0:
  print("You are awesome!")
elif user_choice == 2 and computer_choice == 1:
  print("You've won this round.")
elif user_choice == computer_choice:
  print("It's a draw")
else:
  print("You have lost. Try again")