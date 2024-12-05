#RockPaperScissors
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

#Write your code below this line 👇

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: \n"))

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice >=3 or user_choice < 0:
    print("You choose an invalid number. You lose.")
else:
    print(scissors)

print("\n\nComputer chose: ")
computer_choice = random.randint(0,2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
    print("You Win!")
elif user_choice == computer_choice:
    print("It's a draw.")
else:
    print("You Lose.")

