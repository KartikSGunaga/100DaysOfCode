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
import random

game = ["rock", "paper", "scissors"]

comp_choice = random.randint(0,2)
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("Your choice: " + game[choice])
print("Computer's choice: " + game[comp_choice])

if(comp_choice == choice):
    print("It's a tie")
elif(choice == 2 and comp_choice == 0):
    print("You win!")
elif(choice < comp_choice):
    print("Computer Wins!")
else:
    print("You Win!")