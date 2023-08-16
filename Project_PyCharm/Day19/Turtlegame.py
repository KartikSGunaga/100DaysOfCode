from turtle import Turtle, Screen
import random

screen = Screen()
# tim = Turtle()
# tom = Turtle()
# tum = Turtle()
# tam = Turtle()

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Turtle Racing: Make the Bet', prompt='Choose your turtle: ')
colours = ['red', 'brown', 'green', 'blue', 'black','orange']
start_pos = [-70, -40, -10, 20, 50, 80]
players = []

if(user_bet):
    is_race_on = True

for turtle_player in range(6):
    tim = Turtle(shape = 'turtle')
    tim.color(colours[turtle_player])
    tim.penup()
    tim.goto(x=-230, y=start_pos[turtle_player])
    players.append(tim)

while is_race_on:

    for racer in players:
        if(racer.xcor() > 230):
            is_race_on = False
            winner = racer.pencolor()
            if(user_bet == winner):
                print(f"You won! The {winner} turtle won!")
            else:
                print(f"You lost. The {winner} turtle won!")

        random_dist = random.randint(0,10)
        racer.forward(random_dist)







screen.exitonclick()