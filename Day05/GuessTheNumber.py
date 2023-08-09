import random

print('''Welcome to the number guessing game!
I am thinking of a number between 0-100''')

number = random.randrange(100)

level = input('Enter the difficulty: easy or hard: ').lower()

if(level == 'easy'):
    num_guess = 10
elif(level == 'hard'):
    num_guess = 5
else:
    print('Invalid Entry')

def game_end():
    print(f"You ran out of chances! The number to be guessed was: {number}.")

while(num_guess > 0):
    print(f"You have {num_guess} chances remaining. ")
    guess = int(input('Make a guess: '))

    if(number == guess):
        print(f"You've guessed {number} correctly! There were {num_guess} guesses remaining. ")
        break
    elif(guess < number):
        print("Too low")
        num_guess -= 1
        continue
    else:
        print("Too high")
        num_guess -= 1
        continue

if(num_guess == 0):
        game_end()