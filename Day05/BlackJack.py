import random

# Ask the user if they want to play the game
play = input('Do you want to play the game BlackJack? y or n? ')

# Function to play the BlackJack game
def blackjack():
    # Initialize an empty deck and sums for computer and player
    deck = []
    comp_sum = 0
    hum_sum = 0

    # Card suites
    suites = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

    # Card ranks
    ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

    # Card values
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    # Generate the deck by combining suites and ranks
    for suite in suites:
        for rank in ranks:
            deck.append((rank, suite))

    length = len(deck)

    # Initialize hands for player and computer
    hum = []
    comp = []

    # Randomly choose initial cards for player and computer
    hum_choice1 = random.randrange(length)
    hum_choice2 = random.randrange(length)
    comp_choice1 = random.randrange(length)
    comp_choice2 = random.randrange(length)

    hum.append(deck[hum_choice1]) 
    hum.append(deck[hum_choice2])
    comp.append(deck[comp_choice1])
    comp.append(deck[comp_choice2])

    # Display the player's initial hand and ask for next move
    print(f"Your hand: {hum}.")
    again = input('Press y to get another card (HIT), or press n to continue: ')

    # If player chooses to get another card
    if again == 'y':
        hum_choice2 = random.randrange(length)
        hum[1] = deck[hum_choice2]

    # Calculate the sum of card values for both player and computer
    for value in comp:
        comp_sum += values[value[0]]
    for value in hum:
        hum_sum += values[value[0]]

    # Determine the game outcome based on the sums
    if hum_sum > 21:
        print(f"Computer's hand: {comp}; Your Hand: {hum}")
        print("Computer wins!")
    elif comp_sum > hum_sum:
        print(f"Computer's hand: {comp}; Your Hand: {hum}")
        print("Computer Wins!")
    elif comp_sum == hum_sum:
        print(f"Computer's hand: {comp}; Your Hand: {hum}")
        print("The game is a Tie")
    else:
        print(f"Computer's hand: {comp}; Your Hand: {hum}")
        print("You Win!")

# Start the game if the user chose to play
if play == 'y':
    blackjack()
else:
    print('Thank you for using the interface! ')
